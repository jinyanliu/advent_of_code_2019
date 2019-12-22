"""
Created at 2019-12-22 17:11

@author: jinyanliu
"""
from unittest import TestCase

from days.day_22.day_22 import get_solution_1


class TestDay22(TestCase):
    def test_get_solution_1(self):
        self.assertEqual(7860, get_solution_1())
