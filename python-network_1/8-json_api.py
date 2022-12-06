#!/usr/bin/python3
# a Python script that takes in a letter and sends a POST request to
"""
    http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        value = {"q": ""}
    else:
        value = {"q": sys.argv[1]}
    url = "http://0.0.0.0:5000/search_user"
    result = requests.post(url, data=value)
    try:
        resp = result.json()
        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))
    except ValueError as ve:
        print("Not a valid JSON")
