#!/usr/bin/python3
import json
"""
to_json_string module
"""


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string):
    Args:
        my_obj(str): object
    """
    return json.dumps(my_obj)
