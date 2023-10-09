#!/usr/bin/python3
"""
MyInt that inherits from int:
"""


class MyInt(int):
    """
    class MyInt
    """

    def __eq__(self, other):
        """
        Args:
            other:
        """

        return int(self) is not int(other)

    def __ne__(self, other):
        """
        Args:
            other:
        """
        return int(self) is int(other)
