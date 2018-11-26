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

import bsddb3

__log__ = getLogger(__name__)

operators = {
    ">": operator.gt,
    "<": operator.lt,
    "=": operator.eq,
    ">=": operator.ge,
    "<=": operator.le,
}


def create_temporary_copy(temp_dir, path):
    """Create a tempfile that is a copy of the file specified at the given
    path"""
    temp_path = os.path.join(temp_dir, Path(path).name)
    shutil.copy2(path, temp_path)
    return temp_path


def parse_date(date_string: str):
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

    This loads and interacts with 4 Berkeley Database indexes.
    """

    def __init__(self, ads, terms, pdates, prices, output="brief"):
        """Initialize a query engine by providing paths to the ads, terms,
         pdates, and prices indexes"""
        # create a tempdir and make copies of all the indexes
        self.temp_dir = tempfile.gettempdir()

        ads = create_temporary_copy(self.temp_dir , ads)
        self.ads = bsddb3.hashopen(ads)
        __log__.debug("loaded ads index: {}".format(self.ads))

        terms = create_temporary_copy(self.temp_dir , terms)
        self.terms = bsddb3.btopen(terms)
        __log__.debug("loaded terms index: {}".format(self.terms))

        pdates = create_temporary_copy(self.temp_dir , pdates)
        self.pdates = bsddb3.btopen(pdates)
        __log__.debug("loaded pdates index: {}".format(self.pdates))

        prices = create_temporary_copy(self.temp_dir , prices)
        self.prices = bsddb3.btopen(prices)
        __log__.debug("loaded prices index: {}".format(self.prices))

        if output == "full":
            self.full_output = True
        elif output == "brief":
            self.full_output = False
        else:
            raise ValueError("Invalid argument for output: {}".format(output))

    # TODO: we need the ability to run a query after a query and filter through results
    def run_term_query(self, search_term: str):
        """Print and return all records that have the search_term as a work within
        the title or description fields"""
        __log__.info("starting term query: search_term: {}".format(search_term))
        if search_term.endswith("%"):
            __log__.debug("wildcard detected in search_term: {}".format(search_term))
            base_term = search_term[:-1]
            searching_terms = list((key.decode("utf-8") for key, val in self.terms.items() if re.match(r"{}[a-zA=Z0-9]*".format(base_term), key.decode("utf-8"))))
        else:
            searching_terms = [search_term]

        __log__.info("running search_term query: searching_terms: {}".format(searching_terms))
        for search_term in searching_terms:
            search_term = bytes(search_term, "utf-8")
            if self.terms.has_key(search_term):
                ad_id = self.terms[search_term]
                __log__.info("found matching term: searching_term:{} aid: {} ad: {}".format(search_term, ad_id, self.ads[ad_id].decode("utf-8")))
            else:
                __log__.warning("no matching ad for search_term: {}".format(search_term))
                # TODO allow subqueries to access this data

    def run_cat_query(self, search_category: str):
        # prices and pdates have categories
        __log__.info("running category query: search_category: {}".format(search_category))

        category_matches = set()

        # look through prices
        for price, data in self.prices.items():
            price_str = price.decode("utf-8")
            data_str = data.decode("utf-8")
            db_category = get_category(data_str)
            if db_category == search_category:
                __log__.debug("found matching db_location: {} price: {} data: {}".format(db_category, price_str, data_str))
                category_matches.add(get_aid(data_str))

        # look through dates
        for date, data in self.pdates.items():
            date_str = date.decode("utf-8")
            data_str = data.decode("utf-8")
            db_category = get_category(data_str)
            if db_category == search_category:
                __log__.debug("found matching db_location: {} date: {} data: {}".format(db_category, date_str, data_str))
                category_matches.add(get_aid(data_str))

        for aid in category_matches:
            if self.ads.has_key(bytes(aid, "utf-8")):
                __log__.info("found matching category: search_category: {} aid: {} ad: {}".format(search_category, aid, self.ads[bytes(aid, "utf-8")].decode("utf-8")))
            else:
                __log__.warning("found matching category but no valid full ad relates to the aid: {}".format(aid))
                # TODO allow subqueries to access this data

    def run_location_query(self, search_location: str):
        # prices and pdates have locations

        __log__.info("running location query: search_location: {}".format(search_location))

        location_matches = set()

        # look through prices
        for price, data in self.prices.items():
            price_str = price.decode("utf-8")
            data_str = data.decode("utf-8")
            db_location = get_location(data_str)
            if db_location == search_location:
                __log__.debug("found matching location: {} price: {} data: {}".format(db_location, price_str, data_str))
                location_matches.add(get_aid(data_str))

        # look through dates
        for date, data in self.pdates.items():
            date_str = date.decode("utf-8")
            data_str = data.decode("utf-8")
            db_location = get_location(data_str)
            if db_location == search_location:
                __log__.debug("found matching location: {} date: {} data: {}".format(db_location, date_str, data_str))
                location_matches.add(get_aid(data_str))

        for aid in location_matches:
            if self.ads.has_key(bytes(aid, "utf-8")):
                __log__.info("found matching location: search_location: {} aid: {} ad: {}".format(search_location, aid, self.ads[bytes(aid, "utf-8")].decode("utf-8")))
            else:
                __log__.warning("found matching location but no valid full ad relates to the aid: {}".format(aid))
                # TODO allow subqueries to access this data

    def run_price_query(self, search_price: float, operator):
        __log__.info("running price query: search_price: {} operator: {}".format(search_price, operator))

        price_matches = set()

        for price_str, data in self.prices.items():
            price_str = price_str.decode("utf-8")
            data_str = data.decode("utf-8")
            db_price = float(price_str)
            if operators[operator](search_price, db_price):
                __log__.debug("found valid price: {} data: {}".format(price_str, data_str))
                price_matches.add(get_aid(data_str))

        for aid in price_matches:
            if self.ads.has_key(bytes(aid, "utf-8")):
                __log__.info(
                    "found matching price: {} aid: {} ad: {}".format(search_price, aid, self.ads[bytes(aid, "utf-8")].decode("utf-8")))
            else:
                __log__.warning("found valid price but no valid full ad relates to the aid: {}".format(aid))
                # TODO allow subqueries to access this data

    def run_date_query(self, search_date: datetime.datetime, operator):
        __log__.info("starting date query: search_date: {} operator: {}".format(search_date, operator))

        date_matches = set()

        for date_str, data in self.pdates.items():
            date_str = date_str.decode("utf-8")
            data_str = data.decode("utf-8")
            db_date = parse_date(date_str)
            if operators[operator](search_date, db_date):
                __log__.debug("found valid date: {} data: {}".format(date_str, data_str))
                date_matches.add(get_aid(data_str))

        for aid in date_matches:
            if self.ads.has_key(bytes(aid, "utf-8")):
                __log__.info(
                    "found matching date: {} aid: {} ad: {}".format(search_date, aid, self.ads[bytes(aid, "utf-8")].decode("utf-8")))
            else:
                __log__.warning("found valid date but no valid full ad relates to the aid: {}".format(aid))
                # TODO allow subqueries to access this data


def get_location(data_str: str):
    return data_str.split(",")[2]


def get_category(data_str: str):
    return data_str.split(",")[1]


def get_aid(data_str: str):
    return data_str.split(",")[0]
