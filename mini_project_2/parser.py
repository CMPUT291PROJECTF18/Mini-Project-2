#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import xml.etree.ElementTree as ElementTree


def parse(path_to_file):
    """Parses the inputted XML file. Creates terms.txt, pdates.txt, prices.txt,
    and ads.txt. These text files are used by shell scripts to make Berkeley
    DB index files used for querying."""
    with open(path_to_file, "r") as xml:
        xml_string = xml.read()

    term_string = parse_terms(xml_string)
    create_terms_file(term_string)

    pdate_string = parse_pdates(xml_string)
    create_pdates_file(pdate_string)

    price_string = parse_prices(xml_string)
    create_prices_file(price_string)

    ad_string = parse_ads(xml_string)
    create_ads_file(ad_string)


def parse_terms(xml_string):
    """Parses the XML file to find all keyword terms in the titles and
    descriptions of records."""
    terms = list()

    elem = ElementTree.fromstring(xml_string)
    root = ElementTree.ElementTree(elem).getroot()

    for ad in root.findall("ad"):
        aid = ad.find("aid").text

        title = ad.find("ti").text
        if title is not None:
            title = re.sub("apos;|quot;|\"|'", "", title)

            for token in re.split(r"(?!-)\W", title):
                if len(token) > 2 and re.match(r"^[0-9a-zA-Z_\-]*$", token, 0):
                    terms.append(token.lower() + ":" + aid)

        description = ad.find("desc").text
        if description is not None:
            description = re.sub("apos;|quot;|\"|'", "", description)

            for token in re.split(r"(?!-)\W", description):
                if len(token) > 2 and re.match(r"^[0-9a-zA-Z_\-]*$", token, 0):
                    terms.append(token.lower() + ":" + aid)

    term_string = ""
    for term in terms:
        term_string += (term + "\n")

    return term_string


def create_terms_file(term_string):
    """Creates the terms.txt file."""
    with open("terms.txt", "w") as terms_file:
        terms_file.write(term_string)


def parse_pdates(xml_string):
    """Parses the XML file to make a text file where the keys are the record
    posting dates."""
    pdates = list()

    elem = ElementTree.fromstring(xml_string)
    root = ElementTree.ElementTree(elem).getroot()

    for ad in root.findall("ad"):
        date = ad.find("date").text
        if date is not None:
            aid = ad.find("aid").text
            category = ad.find("cat").text
            location = ad.find("loc").text
            pdates.append(date + ":" + aid + "," + category + "," + location)

    pdate_string = ""
    for pdate in pdates:
        pdate_string += (pdate + "\n")

    return pdate_string


def create_pdates_file(pdate_string):
    """Creates the pdates.txt file."""
    with open("pdates.txt", "w") as pdates_file:
        pdates_file.write(pdate_string)


def parse_prices(xml_string):
    """Parses the XML file to make a text file where the keys are the reocrd
    prices."""
    prices = list()

    elem = ElementTree.fromstring(xml_string)
    root = ElementTree.ElementTree(elem).getroot()

    for ad in root.findall("ad"):
        price = ad.find("price").text
        if price is not None:
            aid = ad.find("aid").text
            category = ad.find("cat").text
            location = ad.find("loc").text
            padding = " " * (12 - len(price))
            prices.append(padding + price + ":" + aid + "," + category + "," +
                          location)

    price_string = ""
    for price in prices:
        price_string += (price + "\n")

    return price_string


def create_prices_file(price_string):
    """Creates the prices.txt file."""
    with open("prices.txt", "w") as prices_file:
        prices_file.write(price_string)


def parse_ads(xml_string):
    """Parses the XML file to create a text file where the keys are the ad IDs
    and the values are the records in XML."""
    ads = list()

    elem = ElementTree.fromstring(xml_string)
    root = ElementTree.ElementTree(elem).getroot()

    for ad in root.findall("ad"):
        aid = ad.find("aid").text
        ads.append(aid + ":")

    for i, ad_xml in enumerate(re.findall("<ad>.*</ad>", xml_string)):
        ads[i] += ad_xml

    ad_string = ""
    for ad in ads:
        ad_string += (ad + "\n")

    return ad_string


def create_ads_file(ad_string):
    """Creates the ads.txt file."""
    with open("ads.txt", "w") as ads_file:
        ads_file.write(ad_string)


if __name__ == "__main__":
    file = input("Path to input data file (XML): ")
    parse(file)
