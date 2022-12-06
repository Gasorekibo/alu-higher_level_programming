#!/usr/bin/python3
# python script that fetches 'https://alu-intranet.hbtn.io/status'
"""
    this will fetch URL
"""
from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen("https://alu-intranet.hbtn.io/status") as f:
        value = f.read()
        print("Body response:")
        print("\t- type: {}".format(type(value)))
        print("\t- content: {}".format(value))
        print("\t- utf8 content: {}".format(value.decode("utf-8")))