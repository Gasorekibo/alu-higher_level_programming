#!/usr/bin/python3
# a python script that print commit from the recent to oldest
""" using two argument name of repository and user_name """
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    request = requests.get(url)
    all_commit = request.json()
    try:
        for p in range(10):
            print("{}: {}".format(all_commit[p].get("sha"),
                 all_commit[p].get("commit").get("author").get("name")))
    except IndexError:
        pass
