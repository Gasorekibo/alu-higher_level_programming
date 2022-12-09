#!/usr/bin/python3
# we are going to use unttest module to test our functions
"""
    first we will import unittest module because it is a builtin function
    and a module that hold our function
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        this is a class that is
        inherit from unittest.TestCase to access all assertion
    """
    def test_ordered(self):
        """
            test ordered list and return max element
        """
        ordered = [4, 5, 6, 7]
        self.assertEqual(max_integer(ordered), 7)

    def test_unordered(self):
        """
            test unordered list
        """
        unordered = [2, 8, 4, 0]
        self.assertEqual(max_integer(unordered), 8)

    def test_empty(self):
        """
            check for empty list
        """
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element(self):
        """
            check for single element in a list
        """
        one = [-10]
        self.assertEqual(max_integer(one), -10)

    def test_float(self):
        """
            checks for list of floating number
        """
        floating_number = [2.3, 5,0, 7.8, 10.0]
        self.assertEqual(max_integer(floating_number), 10.0)

    def test_int_float(self):
        """
            check list containing int and float
        """
        value = [4, 7.9, 0.5, -19]
        self.assertEqual(max_integer(value), 7.9)

    def test_string(self):
        """
            check a list with string
        """
        string = "organization"
        self.assertEqual(max_integer(string), 'z')

    def test_list_string(self):
        """
            checking a list of string
        """
        new = ['hello', 'my', 'people']
        self.assertEqual(max_integer(new), 'people')

    def test_empty_string(self):
        """
            checks for empty string
        """
        self.assertEqual(max_integer(""), None)

    def test_beginning(self):
        """
            checks with max a the beginning
        """
        beg = [98, 7, 2, 0]
        self.assertEqual(max_integer(beg), 98)

    def test_only_negative(self):
        """
            checks only negative number in a list
        """
        neg = [-1, -3, -5, -7]
        self.assertEqual(max_integer(neg), -1)

if __name__ == "__main__":
    unittest.main()
