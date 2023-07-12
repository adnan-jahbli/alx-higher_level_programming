#!/usr/bin/python3
""" This module defines the class 'Student' """


class Student:
    """ This class creates student instances """

    def __init__(self, first_name, last_name, age):
        """ Instance initialization method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ This method returns the directory description """
        return self.__dict__.copy()
