"""
Created at 2019-12-05 19:52

@author: jinyanliu
"""
from enum import Enum


class Opcode(Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    HALT = 99


def get_list_of_int_input():
    with open("day_5_input") as lines:
        list_of_string = lines.readline().split(',')
        list_of_int = [int(s) for s in list_of_string]
    return list_of_int


def get_result_list(integer_input, input_list):
    i = 0
    step = 0
    while i + 1 < len(input_list):

        if input_list[i] == Opcode.ADD.value:
            first_number_position = input_list[i + 1]
            second_number_position = input_list[i + 2]
            replace_position = input_list[i + 3]
            input_list[replace_position] = input_list[first_number_position] + input_list[
                second_number_position]
            step = 3

        elif input_list[i] == Opcode.MULTIPLY.value:
            first_number_position = input_list[i + 1]
            second_number_position = input_list[i + 2]
            replace_position = input_list[i + 3]
            input_list[replace_position] = input_list[first_number_position] * input_list[
                second_number_position]
            step = 3

        elif input_list[i] == Opcode.INPUT.value:
            replace_position = input_list[i + 1]
            input_list[replace_position] = integer_input
            step = 1

        elif input_list[i] == Opcode.OUTPUT.value:
            output_position = input_list[i + 1]
            print(input_list[output_position])

        elif input_list[i] == Opcode.HALT.value:
            break
        i += step + 1

    return input_list



