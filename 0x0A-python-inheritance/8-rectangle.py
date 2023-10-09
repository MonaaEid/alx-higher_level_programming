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


class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Args:
            width(int): integer
            height(int): integer
        """

        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
