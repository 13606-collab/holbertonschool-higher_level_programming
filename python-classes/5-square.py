#!/usr/bin/python3
"""
This module defines a Square class.
It includes validation for size, property handling, and area calculation.
"""


class Square:
    """
    A class that represents a square.

    Attributes:
        __size (int): The side length of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's side (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with type and value validation.

        Args:
            value (int): The new size value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character to stdout.
        If size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print("#" * self.__size)
