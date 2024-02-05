#!/usr/bin/python3
""" Write a class BaseGeometry (based on 6-base_geometry.py). that\n
    validtaes the value and raises exceptions if conditions are not met.
"""


class BaseGeometry:
    """A class with area and integer_validator methods."""
    
    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value and raises exceptions if conditions are not met."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
