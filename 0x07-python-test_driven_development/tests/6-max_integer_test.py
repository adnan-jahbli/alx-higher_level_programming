#!/usr/bin/python3
"""
    Runs Unittest for the max_integer([..]) function
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    
    def test_max_intger(self):
        self.assertEqual(max_integer([18, 20, 2]), 20)
        self.assertEqual(max_integer([20, 20, 20]), 20)
        self.assertEqual(max_integer([20, 20, 30]), 30)
        self.assertEqual(max_integer([-100, 1, 0]), 1)
        self.assertEqual(max_integer([-100, -1, 0]), 0)
        self.assertEqual(max_integer([-100 * -1, -1, 0]), 100)
        self.assertEqual(max_integer([-100, -1, -200]), -1)
        self.assertEqual(max_integer([10]), 10)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([0, 0]), 0)
        self.assertEqual(max_integer([-200]), -200)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([
            92, 93, 93, 94, 95, 96, 97, 98, 99, 100,
            101, 102, 103, 104, 105, 916, 917, 918, 919, 920,
            919, 918, 917, 1000, 915, 914, -913, 912, 911, 910,
            909, 908, 907, -906, 905, 904, 903, 902, 901]), 1000)
    
    def test_list_loop(self):
        list = [2, 4, 6, 8, 10]
        self.assertEqual(max_integer([i * 2 for i in list]), 20)
    
    def test_error_raising(self):
        with self.assertRaises(TypeError):
            max_integer(['1', 2])

        # Test a tuple in an argument
        with self.assertRaises(TypeError):
            max_integer([1, (2, 3)])

        # Test a dictionary in an argument
        with self.assertRaises(KeyError):
            max_integer({"num1": -20, "num2": 100, "num3": 45})

        # Test a single number as argument
        with self.assertRaises(TypeError):
            max_integer(1)
