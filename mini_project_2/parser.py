#!/usr/bin/python
# -*- coding: utf-8 -*-

""""""

from bs4 import BeautifulSoup


xml = input("Give me xml:")

soup = BeautifulSoup(xml, "lxml")