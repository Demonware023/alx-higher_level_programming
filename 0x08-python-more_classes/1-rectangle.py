#!/usr/bin/python3
"""A module that creates a class rectangle which defines a rectangle"""


class Rectangle:
    """A class Rectangle with a real definiton of a rectangle"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    @property
    def width(self):
        return self.__width
    @height.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
