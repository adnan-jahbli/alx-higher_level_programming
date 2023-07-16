#!/usr/bin/python3
""" This module contains the class Square that
inherits from the class Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Child class that inherits from the Rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter method of size attribute """
        return self.width

    @size.setter
    def size(self, new_size):
        """ setter method of size attribute """
        self.width = new_size
        self.height = new_size

    def update(self, *args, **kwargs):
        """ updates the fields of an instance """
        if args:
            self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of an instance fields """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """ return a string representation of an instance """
        msg = "[Square] ({}) {}/{} - {}"
        return msg.format(self.id, self.x, self.y, self.width)
