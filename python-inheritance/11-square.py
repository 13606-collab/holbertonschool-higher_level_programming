#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that represents a square by inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.
        """
        self.integer_validator("size", size)
        """
        Call the parent class (Rectangle) constructor.
        """
        super().__init__(size, size)
        """
        Store the private attribute
        """
        self.__size = size

    def __str__(self):
        """
        Returns the square description.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
