#!/usr/bin/python3
"""fetches X-Request-Id in the response header"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        data = response.json()
        print(data["id"])
    else:
        print("Something went wrong:", response.reason)
