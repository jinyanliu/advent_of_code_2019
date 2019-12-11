"""
Created at 2019-12-11 19:49

@author: jinyanliu
"""

from unittest import TestCase

from days.day_11.day_11 import get_solution_1


class TestDay9(TestCase):
    def test_get_solution_1(self):
        self.assertEqual(2373, get_solution_1())
