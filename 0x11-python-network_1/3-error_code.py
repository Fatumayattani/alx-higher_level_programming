#!/usr/bin/python3
""" Takes in a URL and sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.error
import sys

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
        print(html)
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
