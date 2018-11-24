#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import xml.etree.ElementTree as ElementTree

# xml = input("Give me xml:")

terms = list()
tree = ElementTree.parse("../test/data/10.xml")
root = tree.getroot()
for ad in root.findall("ad"):
    aid = ad.find("aid").text

    titles = ad.find("ti").text
    titles = re.sub("'", "", titles)
    titles = re.sub("\"", "", titles)
    titles = re.sub("&", "", titles)

    for title in re.split("(?!-)\W", titles):
        if len(title) > 2 and re.match("^[0-9a-zA-Z_\-]*$", title, re.M):
            terms.append(title.lower() + ":" + aid)

    descriptions = ad.find("desc").text
    descriptions = re.sub("'", "", descriptions)
    descriptions = re.sub("\"", "", descriptions)
    descriptions = re.sub("&", "", descriptions)

    for desc in re.split("(?!-)\W", descriptions):
        if len(desc) > 2 and re.match("^[0-9a-zA-Z_\-]*$", desc, re.M):
            terms.append(desc.lower() + ":" + aid)

term_string = ""
for term in terms:
    term_string += (term + "\n")

with open("../test/data/10_expected.txt", "r") as expected:
    print(expected.read() == term_string)
