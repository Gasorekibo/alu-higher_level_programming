#!/usr/bin/python3
# a Python script that takes in a URL, sends a request to the URL
"""
    and displays the body of the response using requests module
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    result = request.post(url, data = email)
    print(result.text)
