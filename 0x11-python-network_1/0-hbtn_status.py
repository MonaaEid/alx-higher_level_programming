#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


with urllib.request.urlopen('http://python.org/') as response:
    html = response.read()
