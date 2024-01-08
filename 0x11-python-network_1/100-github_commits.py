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
        # data = response.json()
        # for i in response.json()[:10]:
            # print("{}: {}",i["sha"], i["name"])
            # print("{}: {}".format(i.get('sha'),
            #                     i.get('commit').get('author').get('name')))
        for i in response.json()["commits"][:10]:
            # Print the commit author and sha
            print(f" {i['sha']}: {i['commit']['author']['name']}")
