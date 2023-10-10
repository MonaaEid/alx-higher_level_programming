#!/usr/bin/python3
"""
this read_file module
"""


def read_file(filename=""):
    """
    Args:
        filename: the file name
    """
    with open(filename, 'r') as file:
        print(file.read())
