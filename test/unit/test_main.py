#!/usr/bin/python
# -*- coding: utf-8 -*-

"""pytests for :mod:`.__main__`"""

from mini_project_2.__main__ import get_parser


def test_get_parser():
    parser = get_parser()
    assert parser
