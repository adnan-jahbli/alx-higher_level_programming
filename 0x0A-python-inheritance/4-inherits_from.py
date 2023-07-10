#!/usr/bin/python3
""" This module contains a function that checks if a given object
is an instance of a given class that inherited (directly or indirectly)
from the specified class """


def inherits_from(obj, a_class):
    """ Checks if an object was instantiated from a given class
    that inherited directly or indirectly from the specified class.

    Args:
        obj: the given object
        a_class: the given class

    Returns:
        True or false.
    """
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
