#!/usr/bin/python
# -*- coding: utf-8 -*-

"""pytests for :mod:`.parser`"""

import mini_project_2.parser as parser


def test_parse_terms_10():
    with open("../data/10.xml", "r") as data:
        data_string = data.read()

    term_string = parser.parse_terms(data_string)

    with open("../data/terms_expected_10.txt", "r") as expected:
        expected_string = expected.read()

    assert term_string == expected_string


def test_parse_terms_1000():
    with open("../data/1000.xml", "r") as data:
        data_string = data.read()

    term_string = parser.parse_terms(data_string)

    with open("../data/terms_expected_1000.txt", "r") as expected:
        expected_string = expected.read()

    assert term_string == expected_string


def test_parse_pdates_10():
    with open("../data/10.xml", "r") as data:
        data_string = data.read()

    pdate_string = parser.parse_pdates(data_string)

    with open("../data/pdates_expected_10.txt", "r") as expected:
        expected_string = expected.read()

    assert pdate_string == expected_string


def test_parse_pdates_1000():
    with open("../data/1000.xml", "r") as data:
        data_string = data.read()

    pdate_string = parser.parse_pdates(data_string)

    with open("../data/pdates_expected_1000.txt", "r") as expected:
        expected_string = expected.read()

    assert pdate_string == expected_string
