#!/usr/bin/python3
"""fetches X-Request-Id."""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    params = {"email": email}
    data = urllib.parse.urlencode(params).encode("utf-8")

    with urllib.request.urlopen(url, data) as response:
        body = response.read()
        print(body.decode("utf-8"))
