"""
Created at 2019-12-19 12:06

@author: jinyanliu
"""
from unittest import TestCase

from days.day_19.day_19 import get_solution_1


class TestDay19(TestCase):
    def test_get_solution_1(self):
        self.assertEqual(192, get_solution_1())
