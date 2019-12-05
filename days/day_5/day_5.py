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
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    HALT = 99


class ParametersMode(Enum):
    POSITION = 0
    IMMEDIATE = 1


def get_list_of_int_input():
    with open("day_5_input") as lines:
        list_of_string = lines.readline().split(',')
        list_of_int = [int(s) for s in list_of_string]
    return list_of_int


def get_dict_instruction(digits):
    dict = {}
    if len(str(digits)) > 5:
        print("Opcode more than 5 digits: " + str(digits))

    if len(str(digits)) == 5:
        dict["opcode"] = int(str(digits)[3] + str(digits)[4])
        dict["first_mode"] = int(str(digits)[2])
        dict["second_mode"] = int(str(digits)[1])
        dict["third_mode"] = int(str(digits)[0])


    elif len(str(digits)) == 4:
        dict["opcode"] = int(str(digits)[2] + str(digits)[3])
        dict["first_mode"] = int(str(digits)[1])
        dict["second_mode"] = int(str(digits)[0])
        dict["third_mode"] = 0



    elif len(str(digits)) == 3:
        dict["opcode"] = int(str(digits)[1] + str(digits)[2])
        dict["first_mode"] = int(str(digits)[0])
        dict["second_mode"] = 0
        dict["third_mode"] = 0



    elif len(str(digits)) == 2:
        dict["opcode"] = int(str(digits)[0] + str(digits)[1])
        dict["first_mode"] = 0
        dict["second_mode"] = 0
        dict["third_mode"] = 0


    elif len(str(digits)) == 1:
        dict["opcode"] = digits
        dict["first_mode"] = 0
        dict["second_mode"] = 0
        dict["third_mode"] = 0


    elif len(str(digits)) == 0:
        print("Opcode is empty: " + str(digits))

    return dict


def get_result_list(integer_input, input_list):
    i = 0
    step = 0
    while i + 1 < len(input_list):

        dict_instrction = get_dict_instruction(input_list[i])

        opcode = dict_instrction["opcode"]
        first_mode = dict_instrction["first_mode"]
        second_mode = dict_instrction["second_mode"]
        third_mode = dict_instrction["third_mode"]

        if opcode == Opcode.ADD.value and i + 3 < len(input_list):
            first_value = input_list[input_list[i + 1]] if (first_mode == ParametersMode.POSITION.value) else \
                input_list[i + 1]
            second_value = input_list[input_list[i + 2]] if (second_mode == ParametersMode.POSITION.value) else \
                input_list[i + 2]
            replace_position = input_list[i + 3]
            input_list[replace_position] = first_value + second_value
            step = 3

        elif opcode == Opcode.MULTIPLY.value and i + 3 < len(input_list):
            first_value = input_list[input_list[i + 1]] if (first_mode == ParametersMode.POSITION.value) else \
                input_list[i + 1]
            second_value = input_list[input_list[i + 2]] if (second_mode == ParametersMode.POSITION.value) else \
                input_list[i + 2]
            replace_position = input_list[i + 3]
            input_list[replace_position] = first_value * second_value
            step = 3

        elif opcode == Opcode.INPUT.value:
            replace_position = input_list[i + 1]
            input_list[replace_position] = integer_input
            step = 1

        elif opcode == Opcode.OUTPUT.value:
            output_value = input_list[input_list[i + 1]] if (first_mode == ParametersMode.POSITION.value) else \
                input_list[
                    i + 1]
            print("output_value = " + str(output_value))
            step = 1

        elif opcode == Opcode.HALT.value:
            break
        i += step + 1
    return input_list


def get_solution_1():
    get_result_list(1, get_list_of_int_input())


if __name__ == "__main__":
    get_solution_1()
