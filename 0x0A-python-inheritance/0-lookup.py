#!/usr/bin/python3
"""
This Represent the lookup module
"""


def lookup(obj):
    """
    function that returns the list of
    available attributes and methods of an object
    """

    return [attr for attr in dir(obj) if not callable(getattr(obj, attr))
            and not attr.startswith("__")]
