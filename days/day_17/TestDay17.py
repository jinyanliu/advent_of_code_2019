"""
Created at 2019-12-17 20:03

@author: jinyanliu
"""
from unittest import TestCase

from days.day_17.day_17_part_1 import get_solution_1
from days.day_17.day_17_solution_2 import get_solution_2


class TestDay17(TestCase):
    def test_get_solution_1(self):
        self.assertEqual(8928, get_solution_1())

    def test_get_solution_2(self):
        self.assertEqual(880360, get_solution_2())
