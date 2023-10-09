#!/usr/bin/python3
"""
The add_attribute function
"""


def add_attribute(obj, name, value):
    """
    Args:
        name(str):
        value:
    """

    if hasattr(obj, '__dict__'):
        obj.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
