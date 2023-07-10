#!/usr/bin/python3
""" This module contains a function that checks
if an object is an instance of a specified class """


def is_same_class(obj, a_class):
    """ a function that checks if an object was instantiated
    from a given class.

    Args:
        obj: the given object
        a_class: the specified class

    Returns:
        True if the object is exactly an instance of the
        specified class.
        False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
