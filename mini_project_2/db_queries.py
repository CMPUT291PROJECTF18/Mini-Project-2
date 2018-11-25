#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Database querying engine for part3"""

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
        self.terms = bsddb3.btopen(terms)
        self.pdates = bsddb3.btopen(pdates)
        self.prices = bsddb3.btopen(prices)

        if output == "full":
            self.full_output = True
        elif output == "brief":
            self.full_output = False
        else:
            raise ValueError("Invalid argument for output: {}".format(output))

    # TODO: we need the ability to run a query after a query and filter through results
    def run_term_query(self, term: str):
        __log__.info("running term query: term: {}".format(term))
        if term.endswith("%"):
            __log__.debug("wildcard detected in term: {}".format(term))
            # TODO handle wildcard
        # TODO:

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
