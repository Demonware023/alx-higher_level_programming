#!/usr/bin/python3
""" Write the class Square that inherits from Rectangle this super call\
    will use the logic of the __init__ of the Rectangle class. \
    The width and height must be assigned to the value of size.\
    You must not create new attributes for this class, use all attributes\
    of Rectangle - As reminder: a Square is a Rectangle with \
    the same width and height
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Creates a class sqare that inherits all the attributes from the\
        Rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def display(self):
        """Prints the square with '#' characters."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
