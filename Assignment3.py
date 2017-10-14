#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 3"""

import argparse
import urllib2
import csv
from StringIO import StringIO
import re


def downloadData(url):
    """This function downloads data from a url"""

    data = urllib2.urlopen(url)
    csvdata = data.read()

def parse_csv(csvdata):
    """
    Process the csv data
    :param csvdata:
    :return:percentage of image requests, most popular browser
    """
    count_img = 0
    count_rows = 0
    reader = csv.reader(StringIO(csvdata))

    count_msie = 0
    count_safari = 0
    count_firefox = 0

    for row in reader:
        count_rows += 1
        if re.search("jpg|png|gif", row[0], re.I):
            count_img += 1
        if re.search("MSIE", row[2]):
            count_msie += 1
        if re.search("Safari", row[2]):
            count_safari += 1
        if re.search("Firefox", row[2]):
            count_firefox += 1
    print "The percentage of image requests is",(100 * count_img/count_rows),"%"

    if max(count_firefox, count_msie, count_safari) == count_safari:
        print "The most popular browser today is Safari"
    elif max(count_firefox, count_msie, count_safari) == count_msie:
        print "Internet Explorer"
    elif max(count_firefox, count_msie, count_safari) == count_firefox:
        print "Firefox"
