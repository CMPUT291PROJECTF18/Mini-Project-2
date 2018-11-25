#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import xml.etree.ElementTree as ElementTree


def parse(xml_string):
    term_string = parse_terms(xml_string)
    create_terms_file(term_string)
    pdate_string = parse_pdates(xml_string)
    create_pdates_file(pdate_string)


def parse_terms(xml_string):
    terms = list()

    elem = ElementTree.fromstring(xml_string)
    root = ElementTree.ElementTree(elem).getroot()
    for ad in root.findall("ad"):
        aid = ad.find("aid").text

        title = ad.find("ti").text
        title = re.sub("['\"]", "", title)

        for token in re.split("(?!-)\W", title):
            if len(token) > 2 and re.match("^[0-9a-zA-Z_\-]*$", token, 0):
                terms.append(token.lower() + ":" + aid)

        description = ad.find("desc").text
        description = re.sub("['\"]", "", description)

        for token in re.split("(?!-)\W", description):
            if len(token) > 2 and re.match("^[0-9a-zA-Z_\-]*$", token, 0):
                terms.append(token.lower() + ":" + aid)

    term_string = ""
    for i, term in enumerate(terms):
        if i == len(terms) - 1:
            term_string += term
        else:
            term_string += (term + "\n")

    return term_string


def create_terms_file(term_string):
    # TODO: Implement
    return


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
    for i, term in enumerate(pdates):
        if i == len(pdates) - 1:
            pdate_string += term
        else:
            pdate_string += (term + "\n")

    return pdate_string


def create_pdates_file(pdate_string):
    # TODO: Implement
    return
