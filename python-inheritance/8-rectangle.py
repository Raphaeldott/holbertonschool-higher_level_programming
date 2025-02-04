#!/usr/bin/python3
"""
This module contains one class BaseGeometry and inherited class Rectangle
"""


class BaseGeometry:
    """Class for basic geometry calculation"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        if name is None or not isinstance(name, str):
            raise TypeError("name must be a string")
        if value is None:
            raise TypeError(f"{name} must be an integer")


"""
second class
"""


class Rectangle(BaseGeometry):
    """Inhereted class of BaseGeometry"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
