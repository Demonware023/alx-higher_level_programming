#!/usr/bin/python3
""" A Square Printing Function"""

def print_square(size):
    """
    Prints a square of size length with the character '#'.

    :param size: The size length of the square.
    :raise TypeError: If size is not an integer.
    :raise ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
