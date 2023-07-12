#!/usr/bin/python3
""" This module contains a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object """


def class_to_json(obj):
    """ This function returns the dictionary description of an object

    Args:
        obj: the given object
    """
    dict_d = {}
    if hasattr(obj, "__dict__"):
        dict_t = obj.__dict__.copy()

    return dict_d
