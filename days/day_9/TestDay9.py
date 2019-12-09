"""
Created at 2019-12-09 19:50

@author: jinyanliu
"""

from unittest import TestCase

from days.day_9.day_9 import get_solution_1


class TestDay9(TestCase):
    def test_get_solution_1(self):
        self.assertEqual(3780860499, get_solution_1())
