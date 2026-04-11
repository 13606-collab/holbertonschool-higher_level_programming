#!/usr/bin/python3
"""
This is empty class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

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

    def area(self):
        """
        This method calculates Area of Rectangle
        """
        print(self.__width*self.__hight)
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
