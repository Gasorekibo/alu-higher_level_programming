#!/usr/bin/python3
"""
    importing two module sys and urllib.reques
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as f:
        result = f.read()
        print(result.headers["X-Request-Id"]
