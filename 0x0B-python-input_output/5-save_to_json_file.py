#!/usr/bin/python3
""" This module contains a function that writes an Object to a text file
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """ This function writes an Object to a text file using
        JSON representation..

    Args:
        my_obj: the given Object
        filename: the name of the file to write to
    """
    with open(filename, "r", encoding='utf-8') as f:
        json.dump(my_obj, f)
