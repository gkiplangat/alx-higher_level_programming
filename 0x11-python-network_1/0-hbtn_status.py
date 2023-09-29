#!/usr/bin/python3
""" Python script that fetches an url and prints response body """
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(
            "https://alx-intranet.hbtn.io/status") as request:
        fetched = request.read()
        print("Body response:")
        print(f"\t- type: {type(fetched)}")
        print(f"\t- content: {fetched}")
        print(f"\t- utf8 content: {fetched.decode('utf-8')}")