#!/usr/bin/python3
""" Write a class Rectangle that inherits from \n
    BaseGeometry (7-base_geometry.py).\n
    Instantiation with width and height:\n
    def __init__(self, width, height):\n
    width and height must be private. No getter or setter\n
    width and height must be positive integers, validated\n
    by integer_validator
"""
from 7-base_geometry import BaseGeometry



class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry and represents a rectangle."""

    def __init__(self, width, height):
        """Instantiates a Rectangle object with width and height."""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a string representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
