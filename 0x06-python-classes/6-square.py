#!/usr/bin/python3
"""A square represented by a Square class"""


class Square:
    """Class represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """ initializing the class

        Args:
            size (int): the size of the square
            position (tuple): the position of the square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(type(value) is int and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
