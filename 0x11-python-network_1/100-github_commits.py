#!/usr/bin/python3
"""the module gets
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    response = requests.get(url).json()
    for commit_values in response[:10]:
        commit = commit_values.get('sha')
        owner_name = commit_values.get('commit').get('author').get('name')
        print("{}: {}".format(commit, owner_name))
