"""
Created at 2019-12-17 12:38

@author: jinyanliu
"""
from unittest import TestCase

from days.day_16.day_16_part_1 import get_solution_1


class TestDay16(TestCase):
    def test_get_solution_1(self):
        self.assertEqual("30369587", get_solution_1())
