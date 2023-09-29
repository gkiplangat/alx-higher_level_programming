#!/usr/bin/python3
"""Sending POST request to http://0.0.0.0:5000/search_user."""
from sys import argv
import requests


if __name__ == '__main__':
    letter = {'q': argv[1][0] if len(argv) > 1 else ''}
    r = requests.post('http://0.0.0.0:5000/search_user', data=letter)
    try:
        response = r.json()
        if response:
            print('[{}] {}'.format(response.get('id'), response.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
