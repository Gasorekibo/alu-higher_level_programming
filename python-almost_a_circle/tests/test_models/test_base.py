#!/usr/bin/python3
"""
the unittest of base class that inherit from object
we will import different module to be used here
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase_instantiation(unittest.TestCase):
    """
    a class inherit from TestCase to access different assertio method
    """
    def test_no_arg(self):
        arg1 = Base()
        arg2 = Base()
        self.assertEqual(arg1.id, arg2.id - 1)

    def test_three_bases(self):
        arg1 = Base()
        arg2 = Base()
        arg3 = Base()
        self.assertEqual(arg1.id, arg3.id - 2)

    def test_None_id(self):
        arg1 = Base(None)
        arg2 = Base(None)
        self.assertEqual(arg1.id, arg2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        arg1 = Base()
        arg2 = Base(12)
        arg3 = Base()
        self.assertEqual(arg1.id, arg3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        self.assertEqual("gasore", Base("gasore").id)

    def test_float_id(self):
        self.assertEqual(10.5, Base(10.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(3), Base(complex(3)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([0, 2, 4], Base([0, 2, 4]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(10), Base(range(10)).id)

    def test_bytes_id(self):
        self.assertEqual(b'hello', Base(b'hello').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abce'), Base(bytearray(b'abce')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abce'), Base(memoryview(b'abce')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)
