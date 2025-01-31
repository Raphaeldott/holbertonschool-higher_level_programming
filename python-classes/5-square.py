#!/usr/bin/python3
"""
    A class to represent a square.
    Attributes:
    size : int
        The size of the square (default is 0).

    Methods:
    area():
        Returns the current square area.
    my_print():
        Prints the square with the character '#'.
"""


class Square:
    """kill the coms"""
    def __init__(self, size=0):
        """
        Initializes the square with an optional size.

        Parameters:
        -----------
        size : int
            The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters:
        -----------
        value : int
            The new size of the square.

        Raises:
        -------
        TypeError:
            If value is not an integer.
        ValueError:
            If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square using the '#' character."""
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__size):
            print("#" * self.__size)
