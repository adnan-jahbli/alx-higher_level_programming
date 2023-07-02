#!/usr/bin/python3
"""
This module contains a function that prints
2 new lines after '.', '?' or ':' characters
"""


def text_indentation(text):
    """
    A function that prints 2 new lines after '.', '?' or ':' characters

    Args:
        text (str): input string

    Returns:
        No return value

    Raises:
        TypeError: If the text is not a string
    """
    # validating the input text
    if type(text) != str:
        raise TypeError("text must be a string")

    # declaring variables
    specials = [' ', '\n', '\t']
    str_len = len(text) - 1
    i = 0
    old_c = ''

    for c in text:
        if c in ['.', '?', ':']:
            print(c)
            print()
            old_c = c
        elif c == ' ' and old_c in ['.', '?', ':']:
            old_c = ''
            i += 1
            continue
        elif i < str_len and c == ' ' \
                and (text[i + 1] in specials or text[i - 1] in specials):
            i += 1
            continue
        elif i == len(text) - 1 and c == ' ':
            break
        else:
            print(c, end="")
        i += 1
