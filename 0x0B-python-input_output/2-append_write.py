#!/usr/bin/python3
""" This module includes a function that appends a string at the end
of text file (UTF8) and returns the number of characters added """


def write_file(filename="", text=""):
    """ This function appednds a string at the end of a text file (UTF8).

    Args:
        filename: the name of the file to append to
        text: the text to be appended

    Returns:
        the number of characters added.
    """
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
