#!/usr/bin/python3
"""A square represented by a Square class"""


class Square:
    """Class represents a square"""

    def __init__(self, size=0):
        """ initializing the class

        Args:
            size (int): the size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
