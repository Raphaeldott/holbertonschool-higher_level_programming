#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

"""
task 11
"""


class Square(Rectangle):

    """
    A class that represents a square, inheriting from Rectangle.

    Attributes:
    size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes the square with the given size.

        Args:
        size (int): The size of the square.

        The size is validated to be a positive integer greater than 0.
        """
        self.integer_validator("size", size)  # Validate size
        self._Rectangle__width = size        # Set width
        self._Rectangle__height = size       # Set height

    def __str__(self):
        """
        Returns the string description of the square.
        """
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
