#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Database querying engine for part3"""

import bsddb3


def open_ads_index(path):
    """Open a hash ads index"""
    return bsddb3.hashopen(path)


def open_terms_index(path):
    """Open a B+-tree terms index"""
    return bsddb3.btopen(path)


def open_pdates_index(path):
    """Open a B+-tree pdates index"""
    return bsddb3.btopen(path)


def open_prices_index(path):
    """Open a B+-tree prices index"""
    return bsddb3.btopen(path)
