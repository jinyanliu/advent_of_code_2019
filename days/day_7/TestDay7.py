"""
Created at 2019-12-07 16:17

@author: jinyanliu
"""
from unittest import TestCase

from days.day_7.day_7_part_1 import get_solution_1
from days.day_7.day_7_part_2 import get_solution_2


class TestDay7(TestCase):
    def test_get_solution_1(self):
        self.assertEqual(70597, get_solution_1())

    def test_get_solution_2(self):
        self.assertEqual(30872528, get_solution_2())
