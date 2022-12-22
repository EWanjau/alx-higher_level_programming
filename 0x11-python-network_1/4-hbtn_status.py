#!/usr/bin/python3
"""the module sends a URL request and try except error
"""
import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status").text
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(response), response))
