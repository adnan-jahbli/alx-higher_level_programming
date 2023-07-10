#!/usr/bin/python3
""" This module contains a class "MyList" that
inherits from the built-in class "list" """


class MyList(list):
    """ A childclass of list """
    def print_sorted(self):
        print(sorted(self))
