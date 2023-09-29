#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body."""
import urllib.error
from sys import argv
import urllib.request


if __name__ == "__main__":
    url = argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
