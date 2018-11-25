#!/usr/bin/python
# -*- coding: utf-8 -*-

"""pytests for :mod:`.parser`"""

import mini_project_2.parser as parser
import os


def test_parse_terms_10():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    file = os.path.join(dir_path, "../data/10.xml")
    with open(file, "r") as data:
        data_string = data.read()

    term_string = parser.parse_terms(data_string)

    file = os.path.join(dir_path, "../data/terms_expected_10.txt")
    with open(file, "r") as expected:
        expected_string = expected.read()

    assert term_string == expected_string


def test_parse_terms_1000():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    file = os.path.join(dir_path, "../data/1000.xml")
    with open(file, "r") as data:
        data_string = data.read()

    term_string = parser.parse_terms(data_string)

    file = os.path.join(dir_path, "../data/terms_expected_1000.txt")
    with open(file, "r") as expected:
        expected_string = expected.read()

    assert term_string == expected_string


def test_parse_pdates_10():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    file = os.path.join(dir_path, "../data/10.xml")
    with open(file, "r") as data:
        data_string = data.read()

    pdate_string = parser.parse_pdates(data_string)

    file = os.path.join(dir_path, "../data/pdates_expected_10.txt")
    with open(file, "r") as expected:
        expected_string = expected.read()

    assert pdate_string == expected_string


def test_parse_pdates_1000():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    file = os.path.join(dir_path, "../data/1000.xml")
    with open(file, "r") as data:
        data_string = data.read()

    pdate_string = parser.parse_pdates(data_string)

    file = os.path.join(dir_path, "../data/pdates_expected_1000.txt")
    with open(file, "r") as expected:
        expected_string = expected.read()

    assert pdate_string == expected_string


def test_parse_prices_10():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    file = os.path.join(dir_path, "../data/10.xml")
    with open(file, "r") as data:
        data_string = data.read()

    price_string = parser.parse_prices(data_string)

    file = os.path.join(dir_path, "../data/prices_expected_10.txt")
    with open(file, "r") as expected:
        expected_string = expected.read()

    assert price_string == expected_string


def test_parse_prices_1000():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    file = os.path.join(dir_path, "../data/1000.xml")
    with open(file, "r") as data:
        data_string = data.read()

    price_string = parser.parse_prices(data_string)

    file = os.path.join(dir_path, "../data/prices_expected_1000.txt")
    with open(file, "r") as expected:
        expected_string = expected.read()

    assert price_string == expected_string


def test_parse_ads_10():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    file = os.path.join(dir_path, "../data/10.xml")
    with open(file, "r") as data:
        data_string = data.read()

    ad_string = parser.parse_ads(data_string)

    file = os.path.join(dir_path, "../data/ads_expected_10.txt")
    with open(file, "r") as data:
        expected_string = data.read()

    assert ad_string == expected_string


def test_parse_ads_1000():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    file = os.path.join(dir_path, "../data/1000.xml")
    with open(file, "r") as data:
        data_string = data.read()

    ad_string = parser.parse_ads(data_string)

    file = os.path.join(dir_path, "../data/ads_expected_1000.txt")
    with open(file, "r") as data:
        expected_string = data.read()

    assert ad_string == expected_string
