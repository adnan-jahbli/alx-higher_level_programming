#!/usr/bin/python3
"""
This module contains a function that prints a square with the character #
"""


def print_square(size):
    """
    A function that prints a square with the character #

    Args:
        size (int) : size of the square printed

    Returns:
        No return value

    Raises:
        TypeError: If the size is not an int number
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#' * size)
