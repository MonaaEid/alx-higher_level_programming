#!/usr/bin/python3
"""
save_to_json_file module
"""


import json


def save_to_json_file(my_obj, filename):
    """  writes an Object to a text file, using a JSON representation
    Args:
        my_obj(str): object
        filename: the file name
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
