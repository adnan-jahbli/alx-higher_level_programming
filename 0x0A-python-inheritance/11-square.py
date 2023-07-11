#!/usr/bin/python3
""" a module containing the Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A class that defines a square _from
        the rectangle class
    """
    def __init__(self, size):
        """
           Initializing instance
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
            A methode that returns a string with the calculated area
        """
        return super().area()

    def __str__(self):
        """
            A special method that returns a printable string
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
