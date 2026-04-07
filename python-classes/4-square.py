class Square:
    """Modules that defines a Square"""


    def __init__(self, size=0):
        """
        Initializes the square.

        Args:
            size (int): The side length of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with type and value validation.

        Args:
            value (int): The side length to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value<0:
            raise ValueError("size must be>=0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The area (size squared).
        """
        return self.__size**2
