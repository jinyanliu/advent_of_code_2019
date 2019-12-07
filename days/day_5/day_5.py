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


class InstructionDictKey(Enum):
    OPCODE = "opcode"
    FIRST_MODE = "first_mode"
    SECOND_MODE = "second_mode"
    THIRD_MODE = "third_mode"


def get_list_of_int_input():
    with open("day_5_input") as lines:
        list_of_string = lines.readline().split(',')
        list_of_int = [int(s) for s in list_of_string]
    return list_of_int


def get_dict_instruction(digits):
    instruction_string = str(digits).zfill(5)
    instruction_dict = {InstructionDictKey.OPCODE.value: int(instruction_string[3] + instruction_string[4]),
                        InstructionDictKey.FIRST_MODE.value: int(instruction_string[2]),
                        InstructionDictKey.SECOND_MODE.value: int(instruction_string[1]),
                        InstructionDictKey.THIRD_MODE.value: int(instruction_string[0])}
    return instruction_dict


def get_instructions(instruction_code):
    dict_instruction = get_dict_instruction(instruction_code)
    opcode = dict_instruction[InstructionDictKey.OPCODE.value]
    first_mode = dict_instruction[InstructionDictKey.FIRST_MODE.value]
    second_mode = dict_instruction[InstructionDictKey.SECOND_MODE.value]
    third_mode = dict_instruction[InstructionDictKey.THIRD_MODE.value]
    return opcode, first_mode, second_mode, third_mode


def get_final_output_value(integer_input, input_list):
    i = 0
    step = 0
    output_value = 0
    while i + 1 < len(input_list):
        should_increase_i = True

        opcode, first_mode, second_mode, third_mode = get_instructions(input_list[i])

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

        elif opcode == Opcode.JUMP_IF_TRUE.value:
            step = 2
            first_value = input_list[input_list[i + 1]] if (first_mode == ParametersMode.POSITION.value) else \
                input_list[i + 1]
            if first_value != 0:
                second_value = input_list[input_list[i + 2]] if (second_mode == ParametersMode.POSITION.value) else \
                    input_list[i + 2]
                i = second_value
                should_increase_i = False

        elif opcode == Opcode.JUMP_IF_FALSE.value:
            step = 2
            first_value = input_list[input_list[i + 1]] if (first_mode == ParametersMode.POSITION.value) else \
                input_list[i + 1]
            if first_value == 0:
                second_value = input_list[input_list[i + 2]] if (second_mode == ParametersMode.POSITION.value) else \
                    input_list[i + 2]
                i = second_value
                should_increase_i = False

        elif opcode == Opcode.LESS_THAN.value:
            place_to_store = input_list[i + 3]

            first_value = input_list[input_list[i + 1]] if (first_mode == ParametersMode.POSITION.value) else \
                input_list[i + 1]
            second_value = input_list[input_list[i + 2]] if (second_mode == ParametersMode.POSITION.value) else \
                input_list[i + 2]

            if first_value < second_value:
                input_list[place_to_store] = 1
            else:
                input_list[place_to_store] = 0
            step = 3

        elif opcode == Opcode.EQUALS.value:
            place_to_store = input_list[i + 3]

            first_value = input_list[input_list[i + 1]] if (first_mode == ParametersMode.POSITION.value) else \
                input_list[i + 1]
            second_value = input_list[input_list[i + 2]] if (second_mode == ParametersMode.POSITION.value) else \
                input_list[i + 2]

            if first_value == second_value:
                input_list[place_to_store] = 1
            else:
                input_list[place_to_store] = 0
            step = 3

        elif opcode == Opcode.HALT.value:
            break

        if should_increase_i:
            i += step + 1

    return output_value


def get_solution_1():
    return get_final_output_value(1, get_list_of_int_input())


def get_solution_2():
    return get_final_output_value(5, get_list_of_int_input())


if __name__ == "__main__":
    print(get_solution_1())
    print(get_solution_2())
    print("3"[-3:-2])
