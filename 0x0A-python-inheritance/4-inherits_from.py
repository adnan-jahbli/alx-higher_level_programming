#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ Checks if an object was instantiated _from a given class
    that inherited directly or indirectly _from the specified class.

    Args:
        obj: the given object
        a_class: the given class

    Returns:
        True or false.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
