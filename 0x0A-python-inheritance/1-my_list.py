#!/usr/bin/python3
"""
This List module
"""


class MyList(list):
    """
    This represents MyList class
    """

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
