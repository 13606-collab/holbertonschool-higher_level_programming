#!/usr/bin/python3
"""
This module represents if type(obj) is instance of subclass
"""


def inherits_from(obj, a_class):
    """
    This method return True or False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
