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

    def integer_validator(self, name, value):
        """
        Validates the value to ensure it's a positive integer.

        Args:
            name (str): the name to be used in error messages.
            value (int): the value to be validated.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
