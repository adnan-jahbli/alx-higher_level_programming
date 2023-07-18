#!/usr/bin/python3
""" This module contains a class that defines the class Base """
import json
import csv


class Base:
    """
    Base class for managing id attribute in all other classes.

    Attributes:
        __nb_objects (int): Private class attribute to track the
        number of objects created.
        id (int): Public instance attribute representing the
        unique identifier for each object.

    Methods:
        __init__(self, id=None): Class constructor to initialize
        the id attribute.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the Base class instance.

        Args:
            id (int, optional): Unique identifier for the object.
            If not provided, a new id will be generated based on
            the number of objects created.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Static method that returns a json represenatation
        of a given list """
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class method that saves a list to json file """
        if not list_objs:
            list_objs = []
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w', encoding='utf-8') as f:
            list_d = [obj.to_dictionary() for obj in list_objs]
            f.write(cls.to_json_string(list_d))

    @staticmethod
    def from_json_string(json_string):
        """ Static method that returns a list from a given json string """
        if not json_string or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Creates a new instance from a given dictionary
        containing the values of the instance fields"""
        if cls.__name__ == "Rectangle":
            dummy_obj = cls(2, 1)
        else:
            dummy_obj = cls(2)
        dummy_obj.update(**dictionary)
        return dummy_obj

    @classmethod
    def load_from_file(cls):
        """ Class method that returns a list of instances """
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, 'r', encoding="utf-8") as f:
                json_string = f.read()
                python_list = cls.from_json_string(json_string)
                list_obj = [cls.create(**dic) for dic in python_list]
                return list_obj
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Saves python list to a csv file """
        if not list_objs:
            list_objs = []

        list_d = [obj.to_dictionary() for obj in list_objs]

        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        else:
            fieldnames = ["id", "size", "x", "y"]

        with open(filename, 'w', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(list_d)

    @classmethod
    def load_from_file_csv(cls):
        """ Class method that returns a list of instances """
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, 'r', encoding="utf-8") as f:
                reader = csv.DictReader(f)
                python_list = list(reader)
                # coverting values to int data type instead of str
                for dic in python_list:
                    for key, value in dic.items():
                        dic[key] = int(value)
                # creating new instances and save them in a list
                list_obj = [cls.create(**dic) for dic in python_list]
                return list_obj
        except FileNotFoundError:
            return []
