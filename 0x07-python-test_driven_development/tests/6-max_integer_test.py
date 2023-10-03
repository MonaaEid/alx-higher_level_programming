#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([3, 2, 1]), 3)
        self.assertEqual(max_integer([2, 3, 1]), 3)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([-3, -2, -1]), -1)
        self.assertEqual(max_integer([-2, -3, -1]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3]), 2)
        self.assertEqual(max_integer([3, -2, 1]), 3)
        self.assertEqual(max_integer([2, -3, -1]), 2)

if __name__ == '__main__':
    unittest.main()

