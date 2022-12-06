#!/usr/bin/python3
# a Python script that takes your GitHub credentials username and password
"""
	and uses the GitHub API to display your id
"""
import sys
import requests.auth import HTTPBasicAuth

if __name__ == "__main__":
   user_name = sys.argv[1]
   password sys.argv[2]
   request = get("https://api.github.com/user", auth=auth.HTTPBasicAuth(user_name, password))
   print((request.json().get('id'))
