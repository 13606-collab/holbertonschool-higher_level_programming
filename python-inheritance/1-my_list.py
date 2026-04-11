#!/usr/bin/python3
"""
This module provides a function to list an object's attributes and methods.

"""


class MyList(list):
    """
    This class inherit from list
    """
    def print_sorted(self):
        """
        Prints the list elements in ascending order.
        The original list remains unchanged.
        """

        print(sorted(self))
