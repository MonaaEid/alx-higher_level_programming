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
            raise TypeError("{} must be an integer".format(name))
        
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
