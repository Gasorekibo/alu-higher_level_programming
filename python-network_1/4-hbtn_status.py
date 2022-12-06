#!/usr/bin/python3
# a scrip that fetches the givent url and display the content as string
"""
    fetching the url: https://alu-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    result = requests.get("https://alu-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(result.text)))
    print("\t- content: {}".format(result.text))
