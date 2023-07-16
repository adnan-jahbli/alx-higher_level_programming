#!/usr/bin/python3
""" This module contains the class Rectangle that inherits
from another class Base """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class inherits from Base class
    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): x-coordinate of the rectangle's position.
        y (int): y-coordinate of the rectangle's position.
        id (int): Unique identifier for the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None): Class
        constructor to initialize the Rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the Rectangle class instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the rectangle's
            position (default is 0).
            y (int, optional): y-coordinate of the rectangle's
            position (default is 0).
            id (int, optional): Unique identifier for the rectangle
            (default is None).
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self. __y = y

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, new_width):
        """Setter for the width attribute."""
        if type(new_width) is not int:
            raise TypeError("width must be an integer")
        if new_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_width

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, new_height):
        """Setter for the height attribute."""
        if type(new_height) is not int:
            raise TypeError("height must be an integer")
        if new_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_height

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, new_x):
        """Setter for the x attribute."""
        if type(new_x) is not int:
            raise TypeError("x must be an integer")
        if new_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, new_y):
        """Setter for the y attribute."""
        if type(new_y) is not int:
            raise TypeError("y must be an integer")
        if new_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y

    def area(self):
        """ Calculates and returns the area of the Rectangle instance.

        Returns:
            int: the calculated aread value.
        """
        return self.width * self.height

    def display(self):
        """ prints the Rectangle instance with the character # to stdout """
        for j in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def update(self, *args, **kwargs):
        """ update the values of instance attributes """
        if args:
            self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ return a dictionary representation of an instance attributes """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """ Special method that provides a human-readable string
        representation of the object's state """
        msg = "[Rectangle] ({}) {}/{} - {}/{}"
        return msg.format(self.id, self.x, self.y, self.width, self.height)
