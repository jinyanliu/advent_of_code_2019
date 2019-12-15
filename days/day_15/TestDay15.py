"""
Created at 2019-12-15 19:26

@author: jinyanliu
"""
from unittest import TestCase

from days.day_15.day_15_solution_1 import get_solution_1
from days.day_15.day_15_solution_2 import get_solution_2


class TestDay15(TestCase):
    def test_get_solution_1(self):
        self.assertEqual(308, get_solution_1())

    def test_get_solution_2(self):
        self.assertEqual(328, get_solution_2())
