"""
Created at 2019-12-04 20:41

@author: jinyanliu
"""
from unittest import TestCase

from days.day_4.day_4 import is_sorted, has_multiple_same_adjacent_digits, has_2_same_adjacent_digits, \
    is_matching_extra_condition_in_solution_2, get_answer_to_question_1, get_answer_to_question_2, get_solution_2


class TestDay4(TestCase):

    def test_is_sorted(self):
        self.assertTrue(is_sorted(111111))
        self.assertFalse(is_sorted(223450))
        self.assertTrue(123789)
        self.assertTrue(112233)
        self.assertTrue(123444)
        self.assertTrue(111122)

    def test_has_multiple_same_adjacent_digits(self):
        self.assertTrue(has_multiple_same_adjacent_digits(111111))
        self.assertTrue(has_multiple_same_adjacent_digits(223450))
        self.assertFalse(has_multiple_same_adjacent_digits(123789))

    def test_has_2_same_adjacent_digits(self):
        self.assertTrue(has_2_same_adjacent_digits(112233))
        self.assertFalse(has_2_same_adjacent_digits(123444))
        self.assertTrue(has_2_same_adjacent_digits(111122))

    def test_is_matching_extra_condition_in_solution_2(self):
        self.assertTrue(is_matching_extra_condition_in_solution_2(112233))
        self.assertFalse(is_matching_extra_condition_in_solution_2(123444))
        self.assertTrue(is_matching_extra_condition_in_solution_2(111122))

    def test_get_answer_to_question_1(self):
        self.assertEqual(2090, get_answer_to_question_1())

    def test_get_answer_to_question_2(self):
        self.assertEqual(1419, get_answer_to_question_2())

    def test_get_solution_2(self):
        self.assertEqual(1419, get_solution_2())
