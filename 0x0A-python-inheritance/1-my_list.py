#!/usr/bin/python3
""" A subclass that inherits from list with a sorted method"""


class MyList(list):
    """ The subclass of list with a print_sorted method. """
    def print_sorted(self):
        """Print the list sorted in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
