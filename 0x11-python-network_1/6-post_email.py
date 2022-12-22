#!/usr/bin/python3
"""the module sends a URL request and try except error
"""
import requests
from sys import argv

if __name__ == "__main__":
    value = {'email': argv[2]}
    post_request = requests.post(argv[1], value).text
    print(post_request)
