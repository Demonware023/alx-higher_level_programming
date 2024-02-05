#!/usr/bin/python3
from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry and represents a rectangle."""

    def __init__(self, width, height):
        """Instantiates a Rectangle object with width and height."""
        super().__init__()
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
