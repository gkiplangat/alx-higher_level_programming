#!/usr/bin/python3
""" Holberton School Backend Interview """
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"\
          .format(argv[2], argv[1])
    req = requests.get(url)
    number = 0
    for i in req.json():
        if n < 10:
            print("{}: {}".format(i.get("sha"),
                  i.get("commit").get("author").get("name")))
        number += 1
