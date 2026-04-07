#!/usr/bin/python3
"""
This module defines a Square class.
It handles size and position validation, area calculation, 
and formatted printing with specific coordinates.
"""


class Square:
    """
    A class that represents a square.

    Attributes:
        __size (int): The side length of the square.
        __position (tuple): The (x, y) coordinates of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The side length.
            position (tuple): The horizontal and vertical offset.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position with validation.
        
        Value must be a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with '#' using the position offset.
        - position[1] handles vertical space (newlines).
        - position[0] handles horizontal space (leading spaces).
        """
        if self.__size == 0:
            print("")
            return

        # Print vertical offset (y)
        if self.__position[1] > 0:
            for _ in range(self.__position[1]):
                print("")

        # Print the square rows
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
