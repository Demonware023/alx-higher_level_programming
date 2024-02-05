#!/usr/bin/python3
""" Function that returns the list of available attributes and methods of an     object
"""
def lookup(obj):
    """ functon that returns all the attributes and methods in object"""
    return (dir(obj))
