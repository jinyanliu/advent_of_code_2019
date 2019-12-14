"""
Created at 2019-12-14 20:28

@author: jinyanliu
"""

from unittest import TestCase

from days.day_14.day_14_part_1 import get_solution_1


class TestDay14(TestCase):
    def test_get_solution_1(self):
        self.assertEqual(1037742, get_solution_1())
