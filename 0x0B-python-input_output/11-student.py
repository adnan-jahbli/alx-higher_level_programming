#!/usr/bin/python3
""" This module defines the class 'Student' """


class Student:
    """ This class creates student instances """

    def __init__(self, first_name, last_name, age):
        """ Instance initialization method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ This method returns the directory description """
        dict_d = self.__dict__.copy()
        if type(attrs) is list and \
                all(isinstance(attr, str) for attr in attrs):
            new_dict = {}
            for attr in attrs:
                if attr in dict_d:
                    new_dict[attr] = dict_d[attr]
            dict_d = new_dict.copy()
        return dict_d

    def reload_from_json(self, json):
        """ This method replaces attributes of the Student instance """
        for attr in json:
            self.__dict__[attr] = json[attr]
