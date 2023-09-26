#!/usr/bin/python3
"""Define a MagicClass class"""


import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """

        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError("radius must be a number")
            else:
                self.__radius = int(radius)
        else:
            self.__radius = radius
