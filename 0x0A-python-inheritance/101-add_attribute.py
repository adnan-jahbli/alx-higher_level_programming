#!/usr/bin/python3
""" A module containing the function add_attribute"""


def add_attribute(obj, name, value):
    """
        A function to add a new attribute to an object dynamically

        Args:
            obj: The object to which the attribute will be added
            name: The name of the attribute
            value: The value of the attribute

        Raises:
            TypeError: If the attribute cannot be added to the object
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
