#!/usr/bin/python3
#  a Python script that takes in a URL, sends a request to the URL
"""
    and displays the body of the response using requests package
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    result = requests.get(url)
    if result.status-code >= 400:
        print("Error code: {}".format(result.status_code))
    else:
        print(result.tex)
