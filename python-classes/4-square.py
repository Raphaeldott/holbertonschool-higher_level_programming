#!/usr/bin/python3
"""
A class to represent a square.
Attributes:
__size (int): The size of the square's side.
"""


class Square:
"""too many coms"""
    def __init__(self, size=0):
        """
        Initializes a square with a given size.

        Args:
            size (int, optional): The size of the square's side. Defaults to 0
        """
        self.size = size  # Using the property setter to validate size

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute with validation.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
