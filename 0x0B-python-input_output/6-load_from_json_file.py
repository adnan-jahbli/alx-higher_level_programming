#!/usr/bin/python3
""" This module contains a function that creates
an Object from a JSON file """
import json


def load_from_json_file(filename):
    """ This function that creates an Object from a JSON file..

    Args:
        filename: the name of the file read from
    """
    with open(filename, "r", encoding='utf-8') as f:
        data = json.load(f)
        return data
