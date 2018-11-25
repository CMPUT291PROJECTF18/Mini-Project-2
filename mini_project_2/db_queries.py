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

    def run_query(self, query):
        """Run the given query"""
        __log__.info("running query: {}".format(query))
        # TODO: execute query
