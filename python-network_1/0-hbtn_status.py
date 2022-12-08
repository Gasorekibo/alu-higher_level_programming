#!/usr/bin/python3
# python script that fetches 'https://alu-intranet.hbtn.io/status'
"""
    this will fetch URL
"""
import urllib.request


if __name__ == "__main__":
    result = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(result) as f:
        value = f.read()
        print("Body response:")
        print("\t- type: {}".format(type(value)))
        print("\t- content: {}".format(value))
        print("\t- utf8 content: {}".format(value.decode("utf-8")))
