#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Database querying engine for part3"""
import re
from logging import getLogger

import bsddb3

__log__ = getLogger(__name__)


class QueryEngine:
    """Query processing engine class for part3

    This loads and interacts with 4 Berkeley Database indexes.
    """

    def __init__(self, ads, terms, pdates, prices, output="brief"):
        """Initialize a query engine by providing paths to the ads, terms,
         pdates, and prices indexes"""
        self.ads = bsddb3.hashopen(ads)
        __log__.debug("loaded ads index: {}".format(self.ads))

        self.terms = bsddb3.btopen(terms)
        __log__.debug("loaded terms index: {}".format(self.terms))

        self.pdates = bsddb3.btopen(pdates)
        __log__.debug("loaded pdates index: {}".format(self.pdates))

        self.prices = bsddb3.btopen(prices)
        __log__.debug("loaded prices index: {}".format(self.prices))

        if output == "full":
            self.full_output = True
        elif output == "brief":
            self.full_output = False
        else:
            raise ValueError("Invalid argument for output: {}".format(output))

    # TODO: we need the ability to run a query after a query and filter through results
    def run_term_query(self, term: str):
        """Print and return all records that have the term as a work within
        the title or description fields"""
        __log__.info("starting term query: term: {}".format(term))
        if term.endswith("%"):
            __log__.debug("wildcard detected in term: {}".format(term))
            base_term = term[:-1]
            searching_terms = list((key.decode("utf-8") for key, val in self.terms.items() if re.match(r"{}[a-zA=Z0-9]*".format(base_term), key.decode("utf-8"))))
        else:
            searching_terms = [term]

        __log__.info("running term query: searching_terms: {}".format(searching_terms))
        for term in searching_terms:
            term = bytes(term, "utf-8")
            if self.terms.has_key(term):
                ad_id = self.terms[term]
                __log__.info("found matching term: {} aid: {} ad: {}".format(term, ad_id, self.ads[ad_id]))
                # TODO allow subqueries to access this data


    def run_cat_query(self, cat: str):
        __log__.info("running cat query: cat: {}".format(cat))
        # TODO:

    def run_location_query(self, location: str):
        __log__.info("running location query: location: {}".format(location))
        # TODO:

    def run_price_query(self, price: str, equator):
        __log__.info("running price query: price: {} equator: {}".format(price, equator))
        # TODO:

    def run_date_query(self, date: str, equator):
        # TODO:
        __log__.info("running date query: date: {} equator: {}".format(date, equator))
