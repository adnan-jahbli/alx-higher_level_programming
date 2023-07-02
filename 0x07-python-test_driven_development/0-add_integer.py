#!/usr/bin/python3
"""
    A function that returns the addiction of two numbers
"""


def add_integer(a, b=98):
    """
    Args:
        a: an integer or float number
        b: an integer or float number
    Errors raise:
        TypeError: a must be an integer
        TypeError: b must be an integer
    Return:
        Addition of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
