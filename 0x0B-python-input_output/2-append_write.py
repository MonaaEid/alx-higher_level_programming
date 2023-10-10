#!/usr/bin/python3
"""
append_write module
"""


def append_write(filename="", text=""):
    """
    Args:
        filename: the file name
        text: the string that will be written
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
