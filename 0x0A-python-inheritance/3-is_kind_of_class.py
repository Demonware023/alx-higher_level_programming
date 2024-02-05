#!/usr/bin/python3
""" Write a function that returns True if the object is an instance\n
    of, or if the object is an instance of a class that inherited\n
    from, the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """ Returns true if the object is an instance of, or class inherited"""
    return (isinstance(obj, a_class))
