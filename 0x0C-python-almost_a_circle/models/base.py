#!/usr/bin/python3
""" A base class that takes argument int values, increments if no values
    are given.
"""


class Base:
    """ Defines the class base with id arguments. """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
