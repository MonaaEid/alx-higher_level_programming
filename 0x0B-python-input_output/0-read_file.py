#!/usr/bin/python3
"""
this read_file module
"""


def read_file(filename=""):
    """
    Args:
        filename: the file name
    """
    with open('UTF8', encoding="utf-8") as f:
    read_data = f.read()
    print({}.format(read_data))
