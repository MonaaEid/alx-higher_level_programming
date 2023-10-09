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
            other: anything
        """

        return int(str(self)) is not other

    def __ne__(self, other):
        """
        Args:
            other: anything
        """
        return int(str(self)) is other
