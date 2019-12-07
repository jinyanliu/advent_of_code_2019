"""
Created at 2019-12-07 17:08

@author: jinyanliu
"""

from unittest import TestCase

from days.day_6.day_6_part_1 import get_solution_1
from days.day_6.day_6_part_2 import get_solution_2


class TestDay6(TestCase):
    def test_get_solution_1(self):
        self.assertEqual(162816, get_solution_1())

    def test_get_solution_2(self):
        self.assertEqual(304, get_solution_2())
