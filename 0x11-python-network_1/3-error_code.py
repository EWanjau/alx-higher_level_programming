#!/usr/bin/python3
"""the module sends a URL request and try except error
"""
from urllib import request, error
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            page = response.rea().decode("utf-8")
        print(page)
    except error.HTTPError as error:
        print("Error code: {}".format(error.code))
