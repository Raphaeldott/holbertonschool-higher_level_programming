#!/usr/bin/python3
"""
A class to represent a square.

Attributes:
-----------
size : int
    The size of the square (default is 0).
position : tuple
    The position of the square (default is (0, 0)).

Methods:
--------
area():
    Returns the current square area.

my_print():
    Prints the square with the character '#'.
"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with an optional size and position.

        Parameters:
        -----------
        size : int
            The size of the square (default is 0).
        position : tuple
            The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Gets the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Parameters:
        -----------
        value : tuple
            A tuple of 2 positive integers.

        Raises:
        -------
        TypeError:
            If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square using the '#' character and position."""
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
