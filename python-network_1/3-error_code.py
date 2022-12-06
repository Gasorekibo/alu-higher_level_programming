#!/usr/bin/python3
# a scrip that take in url and display content,
"""
    of the body and  handling differetent error
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as f:
            result = f.read()
            print(result.decode("utf-8"))
    except urllib.error.HTTPError as ex:
        print("Error code: {}".format(ex.code))
