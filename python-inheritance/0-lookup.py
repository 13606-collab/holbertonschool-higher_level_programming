#!/usr/bin/python3
"""
This module provides a function to list an object's attributes and methods.

"""


def lookup(obj):
    """
    Returns a list of attributes and methods.
    
    """
    return dir(obj)
