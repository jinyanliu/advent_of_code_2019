"""
Created at 2019-12-08 12:45

@author: jinyanliu
"""

from unittest import TestCase

from days.day_8.day_8_part_1 import get_solution_1


class TestDay8(TestCase):
    def test_get_solution_1(self):
        self.assertEqual(1905, get_solution_1())
