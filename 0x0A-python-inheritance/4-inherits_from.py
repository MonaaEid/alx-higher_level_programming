#!/usr/bin/python3
"""
This is inherits_from module
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: object
        a_class: class
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
