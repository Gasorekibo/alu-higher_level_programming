#!/usr/bin/python3
# a script that fetches a specific url
""" fetching https://alu-intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request("https://alu-intranet.hbtn.io/status")
    data = with urllib.request.urlopen(req)as f:
        body = f.read()
        print("Body response:")
        print("\t -type : {}".format(type(body)))
        print("\t -content: {}".format(body))
        print("\t -utf8 content: {}".format(body.decode("utf-8")))


