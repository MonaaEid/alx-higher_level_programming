#!/usr/bin/python3
"""fetches X-Request-Id"""
import urllib.request
import sys


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    headers = response.getheaders()
    for header in headers:
        if header[0] == "X-Request-Id":
            print(header[1])
            break
