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
        This method sort inherited file
        """

        return sorted(self)
