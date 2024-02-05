#!/usr/bin/python3
""" Write a function that returns True if the object is an instance\n
    of a class that inherited (directly or indirectly) from the\n
    specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """ Returns true if object is an instance of a class thats inherited\n
        directly/indirectly from a specified class.
    """
    return (isinstance(obj, a_class)) and type(obj) is not a_class
