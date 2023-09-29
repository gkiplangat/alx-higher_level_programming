#!/usr/bin/python3
"""  script that sends a POST request to the passed URL with the email"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urlencode(values)
    data = data.encode('ascii')
    req = Request(url, data, headers={})
    with urlopen(req) as f:
        res = f.read().decode('utf8')
        print(res)
