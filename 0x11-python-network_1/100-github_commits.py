#!/usr/bin/python3
""" github"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(url)


    if response.status_code == 200:
        data = response.json()
        for i in data[:10]:
            # Print the repository information
            print("{}: {}",data["author"], data["name"] )
    # print("{}: {}".format(i.get('sha'),
    #                                 i.get('commit').get('author').get('name')))
