#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """This class represents a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.

    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or position contains negative integers.

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: The size of the square.

        """
        return self._size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """Retrieves the position of the square.

        Returns:
            tuple: The position of the square.

        """
        return self._position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If value contains negative integers.

        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.size ** 2

    def my_print(self):
        """Prints the square with the character # and
        spaces based on its position
        If the size is equal to 0, it prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
