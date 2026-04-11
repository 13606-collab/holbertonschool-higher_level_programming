#!/usr/bin/python3
import math
from abc import ABC, abstractmethod

class Shape(ABC):
    """
    ABC class
    """

    @abstractmethod
    def area(self):
        """Area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Uses duck typing area and perimeter.
    """
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")


# Testing
if __name__ == "__main__":
    my_circle = Circle(5)
    my_rectangle = Rectangle(4, 6)

    print("Circle Info:")
    shape_info(my_circle)
    
    print("\nRectangle Info:")
    shape_info(my_rectangle)
