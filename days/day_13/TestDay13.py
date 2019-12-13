"""
Created at 2019-12-13 22:28

@author: jinyanliu
"""

from unittest import TestCase

from days.day_13.day_13_part_1 import get_solution_1
from days.day_13.day_13_part_2 import get_solution_2


class TestDay13(TestCase):
    def test_get_solution_1(self):
        self.assertEqual(273, get_solution_1())

    def test_get_solution_2(self):
        self.assertEqual(13140, get_solution_2())
