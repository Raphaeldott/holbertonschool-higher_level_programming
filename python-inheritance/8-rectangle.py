#!/usr/bin/python3
"""
Rectangle class that inherits from BaseGeometry.

This class defines a rectangle by its width and height. Both attributes are
validated to ensure they are positive integers. The class also provides a
string representation of the rectangle in the format "[Rectangle]
width/height".
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

        Raises:
            Exception: with the message "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value to ensure it's a positive integer.

        Args:
            name (str): the name to be used in error messages.
            value (int): the value to be validated.

        Raises:
            TypeError: if value is not an integer or is a boolean.
            ValueError: if value is less than or equal to 0.
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

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        super().integer_validator("width", width)  # Utilisation de super()
        super().integer_validator("height", height)
        self.__width = width  # Attribut privé
        self.__height = height  # Attribut privé

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        Returns:
            str: A string in the format "[Rectangle] width/height".
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
