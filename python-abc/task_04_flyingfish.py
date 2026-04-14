#!/usr/bin/python3
"""
Module for Flying fish
"""

class Fish:
    """
    This class is for fish
    """

    def swim(self):
        """Method for swimming"""
        print("The fish is swimming")

    def habitat(self):
        """Method for Habitat"""
        print("The fish lives in water")

class Bird:
    """
    This class is for bird
    """

    def fly(self):
        """Fly"""
        print("The bird is flying")

    def habitat(self):
        """Habitat"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    This class is for flyingfish
    """

    def fly(self):
        """fly method for flyingfish"""
        print("The flying fish is soaring!")

    def swim(self):
        """swim method or flyingfish"""
        print("The flying fish is swimming!")

    def habitat(self):
        """habitat method or flyingfish"""
        print("The flying fish lives both in water and the sky!")
