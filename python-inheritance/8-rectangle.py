#!/usr/bin/python3
'''
This module contains one class BaseGeometry and inherited class Rectangle
'''


class BaseGeometry:
    """Class for basic geometry calculation"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        errors = []
        if isinstance(value, bool):
            errors.append(f"{name} must be an integer")
        if not isinstance(value, int):
            errors.append(f"{name} must be an integer")
        if value is None:
            errors.append(f"{name} must be an integer")
        if isinstance(value, int) and value <= 0:
            errors.append(f"{name} must be greater than 0") 
        if errors:
            raise TypeError("\n".join(errors))


class Rectangle(BaseGeometry):
    """Inherited class of BaseGeometry"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
