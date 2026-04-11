#!/usr/bin/python3
"""
This is empty class
"""


class BaseGeometry:
    """
    Class added
    """

    def area(self):
        """
        This method return a message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method return a message
        """
        self.name = name
        self.value = value

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))

class Rectangle(BaseGeometry):
    """
    This class inheriting from BaseGeometry
    """

    def __init__(self, width, height):
        """
        This method use for Rectangualar
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
