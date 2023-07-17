#!/usr/bin/python3
""" Module for unittesting the Base class """
from io import StringIO
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import unittest
from unittest.mock import patch


class TestBaseMethods(unittest.TestCase):
    """ A test suite to test the Base class """

    def setUp(self):
        """ This method invoked for each test """
        Base._Base__nb_objects = 0

    def test_assigned_id(self):
        """ Test the assigned id """
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_default_id(self):
        """ Test the default id """
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_num_objects(self):
        """ Test a number of objects attribute """
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)

    def test_id_mixed(self):
        """ Test a number of objects attributes and assigned id """
        obj = Base()
        obj2 = Base(1024)
        obj3 = Base()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj2.id, 1024)
        self.assertEqual(obj3.id, 2)

    def test_string_id(self):
        """ Test a string id """
        obj = Base('1')
        self.assertEqual(obj.id, '1')

    def test_more_args_id(self):
        """ Testing to pass more args to the __init__ method """
        with self.assertRaises(TypeError):
            obj = Base(1, 1)

    def test_access_private_attrs(self):
        """ Testing to access private attributes """
        obj = Base()
        with self.assertRaises(AttributeError):
            obj.__nb_objects

    def test_save_to_file(self):
        """ Test the JSON file """
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_1(self):
        """ Test JSON file """
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
