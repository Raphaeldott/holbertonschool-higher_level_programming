#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
Rectangle class that inherits from BaseGeometry.

This class defines a rectangle by its width and height, both of which are
positive integers validated by the integer_validator method. Iy
implements
the area() method to calculate the area of the rectangle and overrides
the __str__ method to provide the rectangle's description in the format
"[Rectangle] width/height".
"""


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    This class defines a rectangle with width and height attributes, both of
    which are validated to be positive integers. It includes a method to
    calculate the area of the rectangle and overrides the __str__ method to
    provide the rectangle's description in format "[Rectangle]width/height".
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
        super().integer_validator("width", width)  # Validate width
        super().integer_validator("height", height)  # Validate height
        self.__width = width  # Private attribute
        self.__height = height  # Private attribute

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        Returns:
            str: A string in the format "[Rectangle] width/height".
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
