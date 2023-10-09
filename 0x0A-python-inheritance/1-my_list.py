#!/usr/bin/python3
"""
This List module
"""


class MyList(list):
    """
    This represents MyList class
    """

    def print_sorted(self):
        """
        prints the list,ascending sort
        """
        sorted_list = sorted(self)
        print(sorted_list)
