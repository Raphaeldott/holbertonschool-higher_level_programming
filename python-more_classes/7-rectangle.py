#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height attributes,
including validation, methods for area and perimeter, string representation,
detection of instance deletion, and tracking the number of instances.
"""


class Rectangle:
    """Defines a rectangle by its width and height."""

    # Class attributes
    number_of_instances = 0
    print_symbol = "#"  # Can be changed to any type

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment instance count

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle using
        print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol)
                          * self.__width] * self.__height)

    def __repr__(self):
        """Return an official string representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when the instance is deleted and decrement
        instance count."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement instance count
