#!/usr/bin/python3
# python script that takes in a URL, sends a request to the URL,
# and display the header content
"""
    sends a request to the URL and displays the value of the X-Request-Id variable found in the header
"""
import sys
import urllib.request.urlopen


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as f:
        result = f.getheader("X-Request-Id")
        print("{}".format(result))
