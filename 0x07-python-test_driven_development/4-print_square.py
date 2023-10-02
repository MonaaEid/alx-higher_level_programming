#!/usr/bin/python3
"""
This is Represent the "print square" module
"""

def print_square(size):
    """
    Print a square shape
    Args:
        size(int): the size oo the square
    Return: Type or Value Error
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
