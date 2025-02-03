#!/usr/bin/python3
from 9-rectangle import Rectangle

"""
Square class that inherits from Rectangle.

This class defines a square with a single size attribute, which is a positive
integer validated by the integer_validator method. The area() method is
implemented and calculates the area of the square using the inherited method
from Rectangle. The string representation is the same format as Rectangle.
"""


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    This class defines a square using a single size attribute. The size is
    validated to be a positive integer. The area() method calculates the
    area of the square using the inherited method from the Rectangle class.
    """

    def __init__(self, size):
        """
        Initializes a new Square object with validated size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)  # Validate size
        self.__size = size  # Private attribute
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return super().area()
