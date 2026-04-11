#!/usr/bin/python3
"""
This module represents if type(obj) is instance of subclass
"""


def is_kind_of_class(obj, a_class):
    """
    This method return True or False
    """
    return issubclass(type(obj), a_class)
