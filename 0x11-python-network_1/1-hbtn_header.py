#!/usr/bin/python3
"""the module sends a URL request and displays variable
"""
from urllib import request
from sys import argv

if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        data = response.info()
    print(data.get('X-Request-Id'))
