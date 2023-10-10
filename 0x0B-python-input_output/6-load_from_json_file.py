#!/usr/bin/python3
"""
from_json_string module
"""


import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”:
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
