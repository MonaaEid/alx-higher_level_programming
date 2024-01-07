#!/usr/bin/python3
"""fetches X-Request-Id in the response header"""
import requests
import sys
from requests.exceptions import HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()

    except HTTPError as http_err:
        print("Error code: {}".format(http_err.code))