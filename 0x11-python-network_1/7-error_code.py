#!/usr/bin/python3
"""fetches X-Request-Id in the response header"""
import requests
import sys
from requests.exceptions import HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
