#!/usr/bin/python3
"""
write_file module
"""

def write_file(filename="", text=""):
    """
    Args:
        filename: the file name
        text: the string that will be written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
