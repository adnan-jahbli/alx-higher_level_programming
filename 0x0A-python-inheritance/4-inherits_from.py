#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ Checks if an object was instantiated from a given class
    that inherited directly or indirectly from the specified class.

    Args:
        obj: the given object
        a_class: the given class

    Returns:
        True or false.
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
