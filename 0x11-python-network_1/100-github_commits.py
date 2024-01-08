#!/usr/bin/python3
""" github"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url)

    if response.status_code == 200:
        for data in response.json()[:10]:
            print(f" {data['sha']}: {data['commit']['author']['name']}")
