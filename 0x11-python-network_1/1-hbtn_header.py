#!/usr/bin/python3
"""fetches X-Request-Id"""
import urllib.request
import sys


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    header = response.headers.get('X-Request-Id')
    print(header)
