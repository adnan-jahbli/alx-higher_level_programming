#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" a module containing the class Rectangle that inherits
from the class BaseGeometry """


class Rectangle(BaseGeometry):
    """ A class that defines a rectangle from
        the BaseGeometry Class
    """

    def __init__(self, width, height):
        """
           Initializing instance
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
