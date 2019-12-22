"""
Created at 2019-12-22 18:19

@author: jinyanliu
"""
from unittest import TestCase

from days.day_21.day_21 import get_solution_1, get_solution_2


class TestDay21(TestCase):
    def test_get_solution_1(self):
        self.assertEqual(19355862, get_solution_1())

    def test_get_solution_2(self):
        self.assertEqual(1140470745, get_solution_2())
