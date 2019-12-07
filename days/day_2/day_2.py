"""
Created at 2019-12-02 19:53

@author: jinyanliu
"""

from enum import Enum


class Opcode(Enum):
    ADD = 1
    MULTIPLY = 2
    HALT = 99


def get_list_of_int_input():
    with open("day_2_input") as lines:
        list_of_string = lines.readline().split(',')
        list_of_int = [int(s) for s in list_of_string]
    return list_of_int


def get_result_list(input_a, input_b, input_list):
    input_list[1] = input_a
    input_list[2] = input_b

    i = 0
    while i + 3 < len(input_list):
        first_number_position = input_list[i + 1]
        second_number_position = input_list[i + 2]
        replace_position = input_list[i + 3]
        if input_list[i] == Opcode.ADD.value:
            input_list[replace_position] = input_list[first_number_position] + input_list[
                second_number_position]

        elif input_list[i] == Opcode.MULTIPLY.value:
            input_list[replace_position] = input_list[first_number_position] * input_list[
                second_number_position]

        elif input_list[i] == Opcode.HALT.value:
            break
        i += 4

    return input_list


def get_first_element_of_result_list(input_a, input_b, input_list):
    return get_result_list(input_a, input_b, input_list)[0]


def get_solution_1():
    return get_first_element_of_result_list(12, 2, get_list_of_int_input())


def get_solution_2():
    for noun in range(100):
        for verb in range(100):
            if get_first_element_of_result_list(noun, verb, get_list_of_int_input()) == 19690720:
                result = 100 * noun + verb
                return result


if __name__ == "__main__":
    print(get_solution_1())
    print(get_solution_2())
