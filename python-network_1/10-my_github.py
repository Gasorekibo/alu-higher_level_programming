#!/usr/bin/python3
# a Python script that takes your GitHub credentials username and password
""" and uses the GitHub API to display your id """
import sys
from  requests.auth import HTTPBasicAuth
import requests


if __name__ == "__main__":
   name = sys.argv[1]
   password = sys.argv[2]
   url = "https://api.github.com/user"
   request = requests.get(url, auth=(name, password))
   print(request.json().get("id"))
