#!/usr/bin/python3
"""
This is the "add two int" module.

The example module supplies one function, add_integer().  For example,

>>> add_integer(5, 5)
10
"""

def add_integer(a, b=98):
    """
    Returns an integer: the addition of a and b
    Args:
        a: first number
        b: second number
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
