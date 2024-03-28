#!/usr/bin/python3
"""the module sends a URL request and a variable as the part of the request
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        value = {'q': ""}
    else:
        value = {'q': argv[1]}
    try:
        response = requests.post("http://0.0.0.0:5000/search_user", value)
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print('No result')
    except ValueError:
        print("Not a valid JSON")
