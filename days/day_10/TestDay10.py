"""
Created at 2019-12-11 20:18

@author: jinyanliu
"""
from unittest import TestCase

from days.day_10.day_10_part_1 import get_solution_1
from days.day_10.day_10_part_2 import get_solution_2


class TestDay10(TestCase):
    def test_get_solution_1(self):
        self.assertEqual(284, get_solution_1())

    def test_get_solution_2(self):
        self.assertEqual(404, get_solution_2())
