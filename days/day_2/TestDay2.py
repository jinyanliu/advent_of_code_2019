"""
Created at 2019-12-07 17:31

@author: jinyanliu
"""
from unittest import TestCase

from days.day_2.day_2 import get_solution_1, get_solution_2


class TestDay2(TestCase):
    def test_get_solution_1(self):
        self.assertEqual(4090701, get_solution_1())

    def test_get_solution_2(self):
        self.assertEqual(6421, get_solution_2())
