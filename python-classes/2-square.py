#!/usr/bin/python3
"""Module that defines a Square"""


class Square:
    """Represents a square with size validation"""

    def __init__(self, size=0):
        """Initialize the square with optional size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
