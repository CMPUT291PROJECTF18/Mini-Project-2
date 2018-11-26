#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Database querying engine for part3"""

import tempfile
import shutil
import os
import operator
from pathlib import Path

import datetime
import re
from logging import getLogger

import lxml
from bs4 import BeautifulSoup
import bsddb3

__log__ = getLogger(__name__)

operators_dict = {
    ">": operator.gt,
    "<": operator.lt,
    "=": operator.eq,
    ">=": operator.ge,
    "<=": operator.le,
}


def create_temporary_copy(temp_dir: str, path: str) -> str:
    """Create a tempfile that is a copy of the file specified at the given
    path"""
    temp_path = os.path.join(temp_dir, Path(path).name)
    shutil.copy2(path, temp_path)
    return temp_path


def parse_date(date_string: str) -> datetime.datetime:
    """Argparse type function for ``date`` query type

    :return: :class:`datetime.datetime` object parsed from the ``date_string``
    """
    try:
        year, month, day = date_string.split("/")
        return datetime.datetime(
            year=int(year),
            month=int(month),
            day=int(day)
        )
    except Exception:
        raise ValueError(
            "invalid date string please follow: 'YYYY/MM/DD"
        )


class QueryEngine:
    """Query processing engine class for part3

    This loads, copies, and then interacts with 4 Berkeley Database indexes
    (``ads.idx``, ``terms.idx``, ``pdates.idx``, and ``prices.idx``).
    """

    def __init__(self, ads: str, terms: str, pdates: str, prices: str,
                 output: str = "brief"):
        """Initialize a query engine by providing paths to the ``ads``,
        ``terms``, ``pdates``, and ``prices`` indexes"""
        # create a tempdir and make copies of all the indexes
        self.temp_dir = tempfile.gettempdir()

        ads = create_temporary_copy(self.temp_dir, ads)
        self.ads = bsddb3.hashopen(ads)
        __log__.debug("loaded ads index: {}".format(self.ads))

        terms = create_temporary_copy(self.temp_dir, terms)
        self.terms = bsddb3.btopen(terms)
        __log__.debug("loaded terms index: {}".format(self.terms))

        pdates = create_temporary_copy(self.temp_dir, pdates)
        self.pdates = bsddb3.btopen(pdates)
        __log__.debug("loaded pdates index: {}".format(self.pdates))

        prices = create_temporary_copy(self.temp_dir, prices)
        self.prices = bsddb3.btopen(prices)
        __log__.debug("loaded prices index: {}".format(self.prices))

        if output == "full":
            self.full_output = True
        elif output == "brief":
            self.full_output = False
        else:
            raise ValueError("Invalid argument for output: {}".format(output))

    def delete_non_matching_aids(self, matching_aids):
        """remove ad(s) from the ads index that do not have a aid contained
        within ``matching_aids``"""
        aids_to_delete = [aid for aid in self.ads.keys() if aid not in [bytes(key, "utf-8") for key in matching_aids]]
        for aid in aids_to_delete:
            self.ads.__delitem__(aid)
        # TODO: we should also cleanup other indexes here aswell
        # this isn't needed functionally, but, if done would likely lead to
        # cleaner code.

    def run_term_query(self, search_term: str):
        """Print and return all records that have the search_term as a
        word within the title or description fields"""
        __log__.info("starting term query: search_term: {}".format(search_term))

        if search_term.endswith("%"):
            __log__.debug("wildcard detected in search_term: {}".format(search_term))
            base_term = search_term[:-1]
            searching_terms = list((key.decode("utf-8").lower() for key, val in self.terms.items() if re.match(r"{}[a-zA-Z0-9\-_]*".format(base_term), key.decode("utf-8"))))
        else:
            searching_terms = [search_term.lower()]

        searching_terms = set(searching_terms)

        __log__.info("running search_term query: searching_terms: {}".format(searching_terms))

        term_matches = set()

        # look through terms
        for term, data in set(self.terms.items()):
            term_str = term.decode("utf-8")
            data_str = data.decode("utf-8")
            if term_str.lower() in searching_terms:
                __log__.info("found matching db_term: {} data: {}".format(term_str, data_str))
                # get the aid from the terms index
                term_matches.add(self.terms[term].decode("utf-8"))
            else:
                self.terms.__delitem__(term)

        for aid in term_matches:
            if self.ads.has_key(bytes(aid, "utf-8")):
                if self.full_output:
                    __log__.info("found matching term: search_term: {} aid: {} ad: {}".format(search_term, aid, self.ads[bytes(aid, "utf-8")].decode("utf-8")))
                else:
                    __log__.info("found matching term: aid: {} title: {}".format(aid, get_title(self.ads[bytes(aid, "utf-8")].decode("utf-8"))))
            else:
                __log__.debug("found matching term but no valid full ad relates to the aid: {}".format(aid))
        self.delete_non_matching_aids(term_matches)
        __log__.info("total hits: {}".format(len(self.ads)))

    def run_cat_query(self, search_category: str):
        """Print all records that have the given ``search_category`` within
        their category fields

        Both the ``prices`` and ``pdates`` indexes have categories thus, they
        will be searched.
        """
        # prices and pdates have categories
        __log__.info("running category query: search_category: {}".format(search_category))

        category_matches = set()

        # look through prices
        for price, data in set(self.prices.items()):
            price_str = price.decode("utf-8")
            data_str = data.decode("utf-8")
            db_category = get_category(data_str)
            if db_category.lower() == search_category.lower():
                __log__.debug("found matching db_location: {} price: {} data: {}".format(db_category, price_str, data_str))
                category_matches.add(get_aid(data_str))
            else:
                self.prices.__delitem__(price)

        # look through dates
        for date, data in set(self.pdates.items()):
            date_str = date.decode("utf-8")
            data_str = data.decode("utf-8")
            db_category = get_category(data_str)
            if db_category.lower() == search_category.lower():
                __log__.debug("found matching db_location: {} date: {} data: {}".format(db_category, date_str, data_str))
                category_matches.add(get_aid(data_str))
            else:
                self.pdates.__delitem__(date)

        for aid in category_matches:
            if self.ads.has_key(bytes(aid, "utf-8")):
                if self.full_output:
                    __log__.info("found matching category: search_category: {} aid: {} ad: {}".format(search_category, aid, self.ads[bytes(aid, "utf-8")].decode("utf-8")))
                else:
                    __log__.info("found matching category: aid: {} title: {}".format(aid, get_title(self.ads[bytes(aid, "utf-8")].decode("utf-8"))))
            else:
                __log__.debug("found matching category but no valid full ad relates to the aid: {}".format(aid))
        self.delete_non_matching_aids(category_matches)
        __log__.info("total hits: {}".format(len(self.ads)))

    def run_location_query(self, search_location: str):
        """Print all records that have the given ``search_location`` within
        their location fields

        Both the ``prices`` and ``pdates`` indexes have locations thus, they
        will be searched.
        """
        __log__.info("running location query: search_location: {}".format(search_location))

        location_matches = set()

        # look through prices
        for price, data in set(self.prices.items()):
            price_str = price.decode("utf-8")
            data_str = data.decode("utf-8")
            db_location = get_location(data_str)
            if db_location.lower() == search_location.lower():
                __log__.debug("found matching location: {} price: {} data: {}".format(db_location, price_str, data_str))
                location_matches.add(get_aid(data_str))
            else:
                self.prices.__delitem__(price)

        # look through dates
        for date, data in set(self.pdates.items()):
            date_str = date.decode("utf-8")
            data_str = data.decode("utf-8")
            db_location = get_location(data_str)
            if db_location.lower() == search_location.lower():
                __log__.debug("found matching location: {} date: {} data: {}".format(db_location, date_str, data_str))
                location_matches.add(get_aid(data_str))
            else:
                self.pdates.__delitem__(date)

        for aid in location_matches:
            if self.ads.has_key(bytes(aid, "utf-8")):
                if self.full_output:
                    __log__.info("found matching location: search_location: {} aid: {} ad: {}".format(search_location, aid, self.ads[bytes(aid, "utf-8")].decode("utf-8")))
                else:
                    __log__.info("found matching location: aid: {} title: {}".format(aid, get_title(self.ads[bytes(aid, "utf-8")].decode("utf-8"))))
            else:
                __log__.debug("found matching location but no valid full ad relates to the aid: {}".format(aid))
        self.delete_non_matching_aids(location_matches)
        __log__.info("total hits: {}".format(len(self.ads)))

    def run_price_query(self, search_price: int, operator_str: str):
        """Print all records that satisfy the equation
        ``record_price operator_str search_price``"""
        __log__.info("running price query: search_price: {} "
                     "operator_str: {}".format(search_price, operator_str))

        price_matches = set()

        # look through prices
        for price, data in set(self.prices.items()):
            price_str = price.decode("utf-8")
            data_str = data.decode("utf-8")
            db_price = int(price_str)
            if operators_dict[operator_str](db_price, search_price):
                __log__.debug("found valid price: {} data: {}".format(price_str, data_str))
                price_matches.add(get_aid(data_str))
            else:
                self.prices.__delitem__(price)

        for aid in price_matches:
            if self.ads.has_key(bytes(aid, "utf-8")):
                if self.full_output:
                    __log__.info("found matching price: {} aid: {} ad: {}".format(search_price, aid, self.ads[bytes(aid, "utf-8")].decode("utf-8")))
                else:
                    __log__.info("found matching price: aid: {} title: {}".format(aid, get_title(self.ads[bytes(aid, "utf-8")].decode("utf-8"))))
            else:
                __log__.debug("found valid price but no valid full ad relates to the aid: {}".format(aid))
        self.delete_non_matching_aids(price_matches)
        __log__.info("total hits: {}".format(len(self.ads)))

    def run_date_query(self, search_date: datetime.datetime,
                       operator_str: str):
        """Print all records that satisfy the equation
        ``record_date operator_str search_date``"""
        __log__.info("starting date query: search_date: {} "
                     "operator_str: {}".format(search_date, operator_str))

        date_matches = set()

        # look through dates
        for date, data in set(self.pdates.items()):
            date_str = date.decode("utf-8")
            data_str = data.decode("utf-8")
            db_date = parse_date(date_str)
            if operators_dict[operator_str](db_date, search_date):
                __log__.debug("found valid date: {} data: {}".format(date_str, data_str))
                date_matches.add(get_aid(data_str))
            else:
                self.pdates.__delitem__(date)

        for aid in date_matches:
            if self.ads.has_key(bytes(aid, "utf-8")):
                if self.full_output:
                    __log__.info("found matching date: {} aid: {} ad: {}".format(search_date, aid, self.ads[bytes(aid, "utf-8")].decode("utf-8")))
                else:
                    __log__.info("found matching date: aid: {} title: {}".format(aid, get_title(self.ads[bytes(aid, "utf-8")].decode("utf-8"))))
            else:
                __log__.debug("found valid date but no valid full ad relates to the aid: {}".format(aid))
        self.delete_non_matching_aids(date_matches)
        __log__.info("total hits: {}".format(len(self.ads)))


def get_location(data_str: str) -> str:
    """Get the category field from either a ``prices`` or ``pdates`` index's
    key's data"""
    return data_str.split(",")[2]


def get_category(data_str: str) -> str:
    """Get the category field from either a ``prices`` or ``pdates`` index's
    key's data"""
    return data_str.split(",")[1]


def get_aid(data_str: str) -> str:
    """Get the ad ID field from either a ``prices`` or ``pdates`` index's
    key's data"""
    return data_str.split(",")[0]


def get_title(ad: str) -> str:
    """From a raw ad records xml extract and return the ads title"""
    soup = BeautifulSoup(ad, "lxml")
    return soup.find("ti").getText()
