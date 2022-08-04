#!/usr/bin/python3
"""the test module for unittest
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class inherits from unittest so that we can use
        assert methods for automatic testing
    """
    def test_max_integer(self):
        """test the function for edge cases, different inputs"""
        self.assertEqual([1, 2, 3, 4], 4)
        self.assertEqual([0, -1, -2, -6], 0)
        self.assertEqual([2.0, 5.0, -1.0, 7.0], 7.0)
        self.assertEqual([10], 10)

    def test_null(self):
        """check for an empty list"""
        self.assertEqual(max_integer([]), None)
