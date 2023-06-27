#!/usr/bin/python3
"""A square represented by a Square class"""


class Square:
    """Class represents a square"""

    def __init__(self, size=0):
        """ initializing the class

        Args:
            size (int): the size of the square
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        for i in range(self.size):
            print("#" * self.size)
