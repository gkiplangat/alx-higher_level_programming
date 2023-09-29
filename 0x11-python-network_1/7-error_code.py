#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body."""
import sys
import requests


if __name__ == "__main__":
    url = argv[1]

    urlReq = requests.get(url)
    if urlReq.status_code >= 400:
        print("Error code: {}".format(urlReq.status_code))
    else:
        print(urlReq.text)
