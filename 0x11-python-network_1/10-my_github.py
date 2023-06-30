#!/usr/bin/python3
"""the module sends a URL request to
   github API and gets the ID from the responses
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/users/{}'.format(argv[1])
    token = argv[2]
    auth_header = {'Authorization': 'token {}'.format(token)}
    response = requests.get(url, headers=auth_header)
    print(response.json().get('id'))
