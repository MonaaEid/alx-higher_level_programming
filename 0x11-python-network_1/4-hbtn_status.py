#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status using request package"""
import requests


if __name__ == "__main__":
    html = requests.get('https://api.github.com')
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
