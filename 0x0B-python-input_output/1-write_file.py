#!/usr/bin/python3
""" This module includes a function that writes a string to a text file
(UTF8) and returns the number of characters written """


def write_file(filename="", text=""):
    """ This function writes a string to a given text file (UTF8).

    Args:
        filename: the name of the file to wrtie to
        text: the text to be written

    Returns:
        the number of characters written.
    """
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
