#!/usr/bin/python3
# a script that takes in URL and email and post request to URL,
"""
    and displays content of the head decoded in utf-8
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    info = urllib.parse.urlencode(email)
    info = info.encode("ascii")
    req = urllib.request.Request(url, info)
    with urllib.request.urlopen(req) as f:
        result = read()
        print(result.decode("utf-8"))
