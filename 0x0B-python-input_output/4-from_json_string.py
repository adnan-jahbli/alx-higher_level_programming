#!/usr/bin/python3
""" This module contains a function that returns an object
(python data structure) represented by JSON string """
import json


def from_json_string(my_str):
    """ This function that returns an object (python data structure)
        represented by JSON string.

    Args:
        my_str: the given string

    Returns:
        An object (python data structure)
    """
    return json.loads(my_str)
