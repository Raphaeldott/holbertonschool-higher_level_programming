#!/usr/bin/python3
"""
Module that defines the BaseGeometry class with area and
integer_validator methods.
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

    def integer_validator(self, name=None, value=None):
        """
        Validates the value to ensure it's a positive integer.

        Args:
            name (str, optional): the name to be used in error messages. Default is None.
            value (int, optional): the value to be validated. Default is None.

        Raises:
            TypeError: if name is not provided or is not a string.
            TypeError: if value is not provided or is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if name is None or not isinstance(name, str):
            raise TypeError("name must be a string")

        if value is None:
            raise TypeError(f"{name} must be an integer")

        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
