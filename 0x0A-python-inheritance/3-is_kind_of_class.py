#!/usr/bin/python3
""" this module includes a function that checks if an object
is an instance of, or if the object is an instance of a class that
inherited from, the specified class """


def is_kind_of_class(obj, a_class):
    """ a function that checks if an object was intantiated from, or
    if the object is an instance of a class that inherited from, the
    specified class.

    Args:
        obj: the given object
        a_class: the given class

    Returns:
        True if the object is an instance of a_class or another class
        that inherited from a_class.
        False otherwise.
    """

    return isinstance(obj, a_class)
