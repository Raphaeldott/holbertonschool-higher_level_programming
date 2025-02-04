#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """
    A class representing base geometry with validation methods.

    Public instance methods:
        - area: raises an exception if not implemented in a subclass.
        - integer_validator: validates integer values.
    """

    def area(self):
        """
        Raises an exception because the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value to ensure it's a positive integer.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        if name is None or not isinstance(name, str):
            raise TypeError("name must be a string")
        if value is None:
            raise TypeError(f"{name} must be an integer")


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
        """
        super().integer_validator("width", width)  # Utilisation de super()
        super().integer_validator("height", height)
        self.__width = width  # Attribut privé
        self.__height = height  # Attribut privé

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
