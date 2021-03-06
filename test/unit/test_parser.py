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

    assert expected_string.strip() == term_string.strip()


def test_parse_terms_1k():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    file = os.path.join(dir_path, "../data/1k.xml")
    with open(file, "r") as data:
        data_string = data.read()

    term_string = parser.parse_terms(data_string)

    file = os.path.join(dir_path, "../data/terms_expected_1k.txt")
    with open(file, "r") as expected:
        expected_string = expected.read()

    assert expected_string.strip() == term_string.strip()


# def test_parse_terms_20k():
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#
#     file = os.path.join(dir_path, "../data/20k.xml")
#     with open(file, "r") as data:
#         data_string = data.read()
#
#     term_string = parser.parse_terms(data_string)
#
#     file = os.path.join(dir_path, "../data/terms_expected_20k.txt")
#     with open(file, "r") as expected:
#         expected_string = expected.read()
#
#     assert expected_string.strip() == term_string.strip()


# def test_parse_terms_100k():
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#
#     file = os.path.join(dir_path, "../data/100k.xml")
#     with open(file, "r") as data:
#         data_string = data.read()
#
#     term_string = parser.parse_terms(data_string)
#
#     file = os.path.join(dir_path, "../data/terms_expected_100k.txt")
#     with open(file, "r") as expected:
#         expected_string = expected.read()
#
#     assert expected_string.strip() == term_string.strip()


def test_parse_pdates_10():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    file = os.path.join(dir_path, "../data/10.xml")
    with open(file, "r") as data:
        data_string = data.read()

    pdate_string = parser.parse_pdates(data_string)

    file = os.path.join(dir_path, "../data/pdates_expected_10.txt")
    with open(file, "r") as expected:
        expected_string = expected.read()

    assert expected_string.strip() == pdate_string.strip()


def test_parse_pdates_1k():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    file = os.path.join(dir_path, "../data/1k.xml")
    with open(file, "r") as data:
        data_string = data.read()

    pdate_string = parser.parse_pdates(data_string)

    file = os.path.join(dir_path, "../data/pdates_expected_1k.txt")
    with open(file, "r") as expected:
        expected_string = expected.read()

    assert expected_string.strip() == pdate_string.strip()


# def test_parse_pdates_20k():
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#
#     file = os.path.join(dir_path, "../data/20k.xml")
#     with open(file, "r") as data:
#         data_string = data.read()
#
#     pdate_string = parser.parse_pdates(data_string)
#
#     file = os.path.join(dir_path, "../data/pdates_expected_20k.txt")
#     with open(file, "r") as expected:
#         expected_string = expected.read()
#
#     assert expected_string.strip() == pdate_string.strip()


# def test_parse_pdates_100k():
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#
#     file = os.path.join(dir_path, "../data/100k.xml")
#     with open(file, "r") as data:
#         data_string = data.read()
#
#     pdate_string = parser.parse_pdates(data_string)
#
#     file = os.path.join(dir_path, "../data/pdates_expected_100k.txt")
#     with open(file, "r") as expected:
#         expected_string = expected.read()
#
#     assert expected_string.strip() == pdate_string.strip()


def test_parse_prices_10():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    file = os.path.join(dir_path, "../data/10.xml")
    with open(file, "r") as data:
        data_string = data.read()

    price_string = parser.parse_prices(data_string)

    file = os.path.join(dir_path, "../data/prices_expected_10.txt")
    with open(file, "r") as expected:
        expected_string = expected.read()

    assert expected_string.strip() == price_string.strip()


def test_parse_prices_1k():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    file = os.path.join(dir_path, "../data/1k.xml")
    with open(file, "r") as data:
        data_string = data.read()

    price_string = parser.parse_prices(data_string)

    file = os.path.join(dir_path, "../data/prices_expected_1k.txt")
    with open(file, "r") as expected:
        expected_string = expected.read()

    assert expected_string.strip() == price_string.strip()


# def test_parse_prices_20k():
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#
#     file = os.path.join(dir_path, "../data/20k.xml")
#     with open(file, "r") as data:
#         data_string = data.read()
#
#     price_string = parser.parse_prices(data_string)
#
#     file = os.path.join(dir_path, "../data/prices_expected_20k.txt")
#     with open(file, "r") as expected:
#         expected_string = expected.read()
#
#     assert expected_string.strip() == price_string.strip()


# def test_parse_prices_100k():
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#
#     file = os.path.join(dir_path, "../data/100k.xml")
#     with open(file, "r") as data:
#         data_string = data.read()
#
#     price_string = parser.parse_prices(data_string)
#
#     file = os.path.join(dir_path, "../data/prices_expected_100k.txt")
#     with open(file, "r") as expected:
#         expected_string = expected.read()
#
#     assert expected_string.strip() == price_string.strip()


def test_parse_ads_10():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    file = os.path.join(dir_path, "../data/10.xml")
    with open(file, "r") as data:
        data_string = data.read()

    ad_string = parser.parse_ads(data_string)

    file = os.path.join(dir_path, "../data/ads_expected_10.txt")
    with open(file, "r") as data:
        expected_string = data.read()

    assert expected_string.strip() == ad_string.strip()


def test_parse_ads_1000():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    file = os.path.join(dir_path, "../data/1k.xml")
    with open(file, "r") as data:
        data_string = data.read()

    ad_string = parser.parse_ads(data_string)

    file = os.path.join(dir_path, "../data/ads_expected_1k.txt")
    with open(file, "r") as data:
        expected_string = data.read()

    assert expected_string.strip() == ad_string.strip()


# def test_parse_ads_20k():
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#
#     file = os.path.join(dir_path, "../data/20k.xml")
#     with open(file, "r") as data:
#         data_string = data.read()
#
#     ad_string = parser.parse_ads(data_string)
#
#     file = os.path.join(dir_path, "../data/ads_expected_20k.txt")
#     with open(file, "r") as data:
#         expected_string = data.read()
#
#     assert expected_string.strip() == ad_string.strip()


# def test_parse_ads_100k():
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#
#     file = os.path.join(dir_path, "../data/100k.xml")
#     with open(file, "r") as data:
#         data_string = data.read()
#
#     ad_string = parser.parse_ads(data_string)
#
#     file = os.path.join(dir_path, "../data/ads_expected_100k.txt")
#     with open(file, "r") as data:
#         expected_string = data.read()
#
#     assert expected_string.strip() == ad_string.strip()
