#!/usr/bin/python3

"""
This module provides a function for adding two integers.
Parameters: a (int or float), b (int or float): Default is 98.
Raises: TypeError: If a or b is not an integer or float.
"""

def add_integer(a, b=98):
    """A function that adds 2 integers a and b. 
    Returns: int: The sum of a and b.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    # Convert to integer if float
    a = int(a)
    b = int(b)

    return (a + b)
