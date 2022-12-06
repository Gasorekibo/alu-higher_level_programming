#!/usr/bin/python3
# a script that fetches a given url
"""
    the script fetches https://alu-intranet.hbtn.io/status
"""
import request


if __name__ == "__main__":
    result = request.get("https://alu-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(result)))
    print("\t- content: {}".format(result))
