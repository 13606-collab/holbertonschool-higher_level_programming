#!/usr/bin/python3
"""
This is empty class
"""


Rectangle = __import__('7-base_geometry').Rectangle


class Square(Rectangle):
    """
    This class defines Square of Rectangle
    """

    def __init__(self, size):
        """
        a new Square instance.
        """
        
        self.integer_validator("size", size)
        """
        weight and height is equal
        """
        super().__init__(size, size)
        """
        size equalize to self.size
        """
        self.__size = size
