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

        return super().__ne__(other)

    def __ne__(self, other):
        """
        Args:
            other: anything
        """
        return super().__eq__(other)
