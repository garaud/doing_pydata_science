# -*- coding: utf-8 -*-

"""Download nyt*.csv files needed in Chapter 2 - Exploratory Data Analysis

Python 3
"""

import os
import requests


URL = "http://stat.columbia.edu/~rachel/datasets"
BASENAME = "nyt{}.csv"
BUFSIZE = 1024
OUTPUT_DIR = "nyt-data"


def download_single_file(number):
    fname = BASENAME.format(number)
    url = '/'.join([URL, fname])
    resp = requests.get(url, stream=True)
    with open(os.path.join(OUTPUT_DIR, fname), 'bw') as fobj:
        for chunk in resp.iter_content(BUFSIZE):
            fobj.write(chunk)


if __name__ == '__main__':
    if not os.path.isdir(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    for n in range(1, 32):
        print("Downloading... file " + BASENAME.format(n))
        download_single_file(n)
