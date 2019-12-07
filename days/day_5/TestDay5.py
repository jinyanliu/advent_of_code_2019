"""
Created at 2019-12-07 17:16

@author: jinyanliu
"""
from unittest import TestCase

from days.day_5.day_5 import get_solution_1, get_solution_2


class TestDay5(TestCase):
    def test_get_solution_1(self):
        self.assertEqual(9219874, get_solution_1())

    def test_get_solution_2(self):
        self.assertEqual(5893654, get_solution_2())
