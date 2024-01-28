#!/usr/bin/python3
""" A name-printing function """

def say_my_name(first_name, last_name=""):
    """
    Prints a name(formatted string "My name is <first name> <last name>".

    param first_name: The first name (required).
    parm last_name: The last name (optional, defaults to an empty string).

    Raise: TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

