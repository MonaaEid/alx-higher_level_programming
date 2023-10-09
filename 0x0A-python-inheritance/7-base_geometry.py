#!/usr/bin/python3
"""
A class BaseGeometry.
"""


class BaseGeometry:
    """
    class BaseGeometry
    """

    def area(self):
        """
        function that raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method validates the value of an integer argument
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
