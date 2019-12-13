"""
Created at 2019-12-13 22:31

@author: jinyanliu
"""
from unittest import TestCase

from days.day_12.day_12_part_1 import get_solution_1


class TestDay12(TestCase):
    def test_get_solution_1(self):
        self.assertEqual(9493, get_solution_1())
