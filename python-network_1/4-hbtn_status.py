#!/usr/bin/python3
# a script that fetches a given url
"""
    the script fetches https://alu-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    with ullib.request.urlopen("https://alu-intranet.hbtn.io/status") as f:
        result = f.read()
        print("Body response:")
        print("\t- type: {}".format(type(result)))
        print("\t- content: {}".format(result))
