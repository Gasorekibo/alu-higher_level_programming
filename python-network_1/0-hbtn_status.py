#!/usr/bin/python3
# fetching a specific url given
"""
   we are going to fetch https://alu-intranet.hbtn.io/status as url given
"""
from urllib.request import urllopen


if __name__ == "__main__":
    with urlopen("https://alu-intranet.hbtn.io/status") as f:
        value = f.read()
        print("Body response:")
        print("\t - type: {}".format(type(value)))
        print("\t - content: {}".format(value))
        print("\t - utf8 content: {}".format(value.decode("utf-8")))
