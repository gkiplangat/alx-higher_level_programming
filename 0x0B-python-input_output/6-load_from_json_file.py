#!/usr/bin/python3

"""
6-load_from_json_file.py
defining load_from_json_file function
"""


import json


def load_from_json_file(filename):
    """
    creates an object from json file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
