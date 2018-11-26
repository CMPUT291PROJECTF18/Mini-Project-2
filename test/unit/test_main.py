#!/usr/bin/python
# -*- coding: utf-8 -*-

"""pytests for :mod:`.__main__`"""
import argparse

import pytest

from mini_project_2.__main__ import get_parser, main, alpha_numeric, \
    term_alpha_numeric


def test_get_parser():
    parser = get_parser()
    assert parser


@pytest.mark.parametrize("cmd",
                         [
                             "price>-30 term=camera",
                             "price>0 term=camera",
                             "price<30 term=camera",
                             "price=30",
                             "price>=30",
                             "price<=30",
                             "price<30",
                             "price>30",
                             "term=camera",
                             "term=camera%",
                             "location=Red-deer",
                             "location=Calgary",
                             "price>30 term=camera location=Calgary",
                             "price>30 term=camera location=Red-Deer",
                             "price>30 term=camera location=Red-Deer cat=nonsuchcat",
                             "cat=nonsuchcat",
                             "date=2018/01/01",
                             "date>=2018/01/01",
                             "date<=2018/01/01",
                             "date>2018/01/01",
                             "date<2018/01/01",
                             "price>30 term=camera location=Red-Deer cat=nonsuchcat date>2018/01/01",
                             # given queries to test
                             "term=camera",
                             "term=camera%",
                             "date<=2018/11/05",
                             "date>2018/11/05",
                             "price<20",
                             "price>=20",
                             "location=edmonton date=2018/11/07",
                             "cat=art-collectibles term=camera",
                             "term=camera date>=2018/11/05 date<=2018/11/07 price>20 price<40"
                         ]
                         )
def test_main(cmd):
    """Bad tests to ensure nothing is extremely broken"""
    base_cmd = """-ad mini_project_2/scripts/data/indexes/ads.idx -te mini_project_2/scripts/data/indexes/terms.idx -da mini_project_2/scripts/data/indexes/pdates.idx -pr mini_project_2/scripts/data/indexes/prices.idx -o full -v --log-level INFO"""
    main(base_cmd.split() + cmd.split())
    # TODO: more better testing.


@pytest.mark.parametrize("alpha_numeric_str",
                         [
                             "a",
                             "z"
                             "1",
                             "A",
                             "Z",
                             "-",
                             "_",
                             "ABC123abc-_",
                             "A-b"
                         ]
                         )
def test_alpha_numeric(alpha_numeric_str):
    assert alpha_numeric(alpha_numeric_str)


@pytest.mark.parametrize("non_alpha_numeric_str",
                         [
                             "",
                             "Ð"
                             "*",
                             "{}}",
                             "a*"
                             "b???/",
                             "125$$@#22",
                             "+‗",
                             "'",
                             "\\",
                             "//"
                         ]
                         )
def test_alpha_numeric_fail(non_alpha_numeric_str):
    with pytest.raises(argparse.ArgumentTypeError):
        alpha_numeric(non_alpha_numeric_str)


@pytest.mark.parametrize("term_alpha_numeric_str",
                         [
                             "a",
                             "z"
                             "1",
                             "A",
                             "Z",
                             "-",
                             "_",
                             "ABC123abc-_",
                             "A-b",
                             "a%",
                             "z%",
                             "1%",
                             "A%",
                             "Z%",
                             "-%",
                             "_%",
                             "ABC123abc-_%",
                             "A-b%"
                         ]
                         )
def test_term_alpha_numeric(term_alpha_numeric_str):
    assert term_alpha_numeric(term_alpha_numeric_str)


@pytest.mark.parametrize("term_alpha_numeric_str",
                         [
                             "",
                             "Ð"
                             "*",
                             "{}}",
                             "a*"
                             "b???/",
                             "125$$@#22",
                             "+‗",
                             "'",
                             "\\",
                             "//",
                             "%1%",
                             "_&&6%",
                             "ABC1^^^23abc-_%",
                         ]
                         )
def test_term_alpha_numeric_fail(term_alpha_numeric_str):
    with pytest.raises(argparse.ArgumentTypeError):
        assert term_alpha_numeric(term_alpha_numeric_str)
