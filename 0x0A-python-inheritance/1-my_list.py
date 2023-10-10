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
        #sorted_list = sorted(self)
        sorted_list = self[:]
        sorted_list.sort()
        print("{}".format(sorted_list))
