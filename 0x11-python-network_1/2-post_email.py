#!/usr/bin/python3
"""  Sends POST request to passed URL with email"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    value = {'email': email}
    data = urlencode(value)
    data = data.encode('ascii')
    request = Request(url, data, headers={})
    with urlopen(request) as f:
        response = f.read().decode('utf8')
        print(response)
