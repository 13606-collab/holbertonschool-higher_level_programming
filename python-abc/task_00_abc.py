#!/usr/bin/python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    An abstract base class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses to return a sound.
        """
        pass


class Dog(Animal):
    """
    A subclass of Animal representing a dog.
    """

    def sound(self):
        """
        Returns the sound a dog makes.
        """
        return "Bark"


class Cat(Animal):
    """
    A subclass of Animal representing a cat.
    """

    def sound(self):
        """
        Returns the sound a cat makes.
        """
        return "Meow"
