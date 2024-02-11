#!/usr/bin/python3
""" Write the class Rectangle that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ Write the class Rectangle that inherits from Base with private
        attributes set and and implementing getters and setters for them.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def update(self, *args, **kwargs):
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, attr in enumerate(args):
                setattr(self, attrs[i], attr)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)
