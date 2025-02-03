#!/usr/bin/python3
from 7-base_geometry import BaseGeometry

"""
Rectangle class that inherits from BaseGeometry.

This class defines a rectangle by its width and height. Both attributes are
validated to ensure they are positive integers. The class also provides a
string representation of rectangle in the format "[Rectangle] width/height".
"""


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    This class defines a rectangle by its width and height, both of which are
    validated to ensure they are positive integers. It also includes a string
    representation method to display the rectangle's dimensions.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle object with validated width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)  # Validate width
        self.integer_validator("height", height)  # Validate height
        self.__width = width  # Private attribute
        self.__height = height  # Private attribute

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        Returns:
            str: A string in the format "[Rectangle] width/height".
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
