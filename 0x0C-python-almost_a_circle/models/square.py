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
    def __init__(self, size, x=0, y=0,id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size attribute."""
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns the spring reprsentaion of the square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
