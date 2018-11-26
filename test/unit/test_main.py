#!/usr/bin/python
# -*- coding: utf-8 -*-

"""pytests for :mod:`.__main__`"""
import argparse

import pytest

from mini_project_2.__main__ import get_parser, main, alpha_numeric


def test_get_parser():
    parser = get_parser()
    assert parser


@pytest.mark.parametrize("cmd",
    [
        "price>-30 term=camera".split(),
        "price>0 term=camera".split(),
        "price<30 term=camera".split(),
        "price=30".split(),
        "price>=30".split(),
        "price<=30".split(),
        "price<30".split(),
        "price>30".split(),
        "term=camera".split(),
        "term=camera%".split(),
        "location=Red-deer".split(),
        "location=Calgary".split(),
        "price>30 term=camera location=Calgary".split(),
        "price>30 term=camera location=Red-Deer".split(),
        "price>30 term=camera location=Red-Deer cat=nonsuchcat".split(),
        "cat=nonsuchcat".split(),
        "date=2018/01/01".split(),
        "date>=2018/01/01".split(),
        "date<=2018/01/01".split(),
        "date>2018/01/01".split(),
        "date<2018/01/01".split(),
        "price>30 term=camera location=Red-Deer cat=nonsuchcat date>2018/01/01".split(),
    ]
)
def test_main(cmd):
    """Bad tests to ensure nothing is extremely broken"""
    base_cmd = """-ad mini_project_2/scripts/data/indexes/ads.idx -te mini_project_2/scripts/data/indexes/terms.idx -da mini_project_2/scripts/data/indexes/pdates.idx -pr mini_project_2/scripts/data/indexes/prices.idx -o full -v --log-level INFO""".split()
    main(base_cmd+cmd)
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