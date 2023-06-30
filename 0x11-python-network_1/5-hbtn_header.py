#!/usr/bin/python3
"""the module sends a URL request and try except error
"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1]).headers
    print(response.get('X-Request-Id'))
