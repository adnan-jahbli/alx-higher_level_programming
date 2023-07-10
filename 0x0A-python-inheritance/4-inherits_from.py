#!/usr/bin/python3
""" a module containing one function """


def inherits_from(obj, a_class):
    """ Checks if an object is an instance of a given class
    that inherited directly or indirectly the specified class.

    Args:
        obj: the given object
        a_class: the given class

    Returns:
        True or false.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
