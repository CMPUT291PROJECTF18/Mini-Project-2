#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import xml.etree.ElementTree as ElementTree


def parse(xml_string):
    term_string = parse_terms(xml_string)
    create_terms_file(term_string)

    pdate_string = parse_pdates(xml_string)
    create_pdates_file(pdate_string)

    price_string = parse_prices(xml_string)
    create_prices_file(price_string)

    ad_string = parse_ads(xml_string)
    create_ads_file(ad_string)


def parse_terms(xml_string):
    terms = list()

    elem = ElementTree.fromstring(xml_string)
    root = ElementTree.ElementTree(elem).getroot()

    for ad in root.findall("ad"):
        aid = ad.find("aid").text

        title = ad.find("ti").text
        title = re.sub("['\"]", "", title)

        for token in re.split(r"(?!-)\W", title):
            if len(token) > 2 and re.match(r"^[0-9a-zA-Z_\-]*$", token, 0):
                terms.append(token.lower() + ":" + aid)

        description = ad.find("desc").text
        description = re.sub("['\"]", "", description)

        for token in re.split(r"(?!-)\W", description):
            if len(token) > 2 and re.match(r"^[0-9a-zA-Z_\-]*$", token, 0):
                terms.append(token.lower() + ":" + aid)

    term_string = ""
    for i, term in enumerate(terms):
        if i == len(terms) - 1:
            term_string += term
        else:
            term_string += (term + "\n")

    return term_string


def create_terms_file(term_string):
    with open("terms.txt", "w") as terms_file:
        terms_file.write(term_string)


def parse_pdates(xml_string):
    pdates = list()

    elem = ElementTree.fromstring(xml_string)
    root = ElementTree.ElementTree(elem).getroot()

    for ad in root.findall("ad"):
        date = ad.find("date").text
        aid = ad.find("aid").text
        category = ad.find("cat").text
        location = ad.find("loc").text
        pdates.append(date + ":" + aid + "," + category + "," + location)

    pdate_string = ""
    for i, pdate in enumerate(pdates):
        if i == len(pdates) - 1:
            pdate_string += pdate
        else:
            pdate_string += (pdate + "\n")

    return pdate_string


def create_pdates_file(pdate_string):
    with open("pdates.txt", "w") as pdates_file:
        pdates_file.write(pdate_string)


def parse_prices(xml_string):
    prices = list()

    elem = ElementTree.fromstring(xml_string)
    root = ElementTree.ElementTree(elem).getroot()

    for ad in root.findall("ad"):
        price = ad.find("price").text
        if len(price):
            aid = ad.find("aid").text
            category = ad.find("cat").text
            location = ad.find("loc").text
            prices.append(price + ":" + aid + "," + category + "," + location)

    price_string = ""
    for i, price in enumerate(prices):
        if i == len(prices) - 1:
            price_string += price
        else:
            price_string += (price + "\n")

    return price_string


def create_prices_file(price_string):
    with open("prices.txt", "w") as prices_file:
        prices_file.write(price_string)


def parse_ads(xml_string):
    ads = list()

    elem = ElementTree.fromstring(xml_string)
    root = ElementTree.ElementTree(elem).getroot()

    for ad in root.findall("ad"):
        aid = ad.find("aid").text
        ads.append(aid + ":")

    for i, ad_xml in enumerate(re.findall("<ad>.*</ad>", xml_string)):
        ads[i] += ad_xml

    ad_string = ""
    for i, ad in enumerate(ads):
        if i == len(ads) - 1:
            ad_string += ad
        else:
            ad_string += (ad + "\n")

    return ad_string


def create_ads_file(ad_string):
    with open("ads.txt", "w") as ads_file:
        ads_file.write(ad_string)
