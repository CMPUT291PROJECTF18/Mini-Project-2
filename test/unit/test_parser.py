#!/usr/bin/python
# -*- coding: utf-8 -*-

"""pytests for :mod:`.parser`"""

import mini_project_2.parser as parser


def test_parse_terms():
    with open("../data/10.xml", "r") as data:
        data_string = data.read()

    term_string = parser.parse_terms(data_string)

    with open("../data/10_expected.txt", "r") as expected:
        expected_string = expected.read()

    assert term_string == expected_string


