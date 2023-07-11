#!/usr/bin/python3
""" This module contains the class MyInt """


class MyInt(int):
    """
        Custom class that extends the functionality
        of the built-in int class
    """
    def __eq__(self, other):
        """
            Override the == operator to perform the != check
        """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """
            Override the != operator to perform the == check
        """
        return int.__eq__(self, other)
