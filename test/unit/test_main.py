#!/usr/bin/python
# -*- coding: utf-8 -*-

"""pytests for :mod:`.__main__`"""

import pytest

from mini_project_2.__main__ import get_parser, main


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
