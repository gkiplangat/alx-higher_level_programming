#!/usr/bin/python3
""" Send POST request to URL with the email as a parameter"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = {'email': email}
    res = requests.post(url, data=data)
    print(res.text)
