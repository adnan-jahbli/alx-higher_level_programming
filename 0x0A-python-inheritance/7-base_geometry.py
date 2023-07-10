#!/usr/bin/python3
""" a module containing the class BaseGeometry """


class BaseGeometry:
    """ Empty class """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ A method that recieves the value property

        Args:
            name: the name of the object
            value: the value of the property
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
