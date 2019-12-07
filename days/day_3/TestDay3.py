"""
Created at 2019-12-07 17:28

@author: jinyanliu
"""
from unittest import TestCase

from days.day_3.day_3 import get_answer_to_question_1, get_answer_to_question_2


class TestDay3(TestCase):
    def test_get_answer_to_question_1(self):
        self.assertEqual(529, get_answer_to_question_1())

    def test_get_answer_to_question_2(self):
        self.assertEqual(20386, get_answer_to_question_2())
