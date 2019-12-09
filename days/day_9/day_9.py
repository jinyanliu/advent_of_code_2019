"""
Created at 2019-12-09 19:00

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
    RELATIVE_BASE = 9
    HALT = 99


class ParametersMode(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class InstructionDictKey(Enum):
    OPCODE = "opcode"
    FIRST_MODE = "first_mode"
    SECOND_MODE = "second_mode"
    THIRD_MODE = "third_mode"


def get_dict_of_int_input():
    dict_of_int_input = {}
    i = 0
    with open("day_9_input") as lines:
        list_of_string = lines.readline().split(',')
        for s in list_of_string:
            dict_of_int_input[i] = int(s)
            i += 1
    print(dict_of_int_input)
    return dict_of_int_input


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


def get_value(mode, input_dict, i, relative_base, number):
    if mode == ParametersMode.POSITION.value:
        return input_dict[input_dict[i + number]] if input_dict[i + number] in input_dict.keys() else 0
    elif mode == ParametersMode.IMMEDIATE.value:
        return input_dict[i + number]
    elif mode == ParametersMode.RELATIVE.value:
        relative_position = relative_base + input_dict[i + number]
        return input_dict[relative_position]


def get_replace_position(mode, input_dict, i, relative_base, number):
    if mode == ParametersMode.POSITION.value:
        return input_dict[i + number]
    elif mode == ParametersMode.RELATIVE.value:
        return relative_base + input_dict[i + number]


def get_output(list_of_input_integers, input_dict):
    i = 0
    step = 0
    output_value = None
    relative_base = 0
    while i + 1 < len(input_dict):
        should_increase_i = True

        opcode, first_mode, second_mode, third_mode = get_instructions(input_dict[i])

        if opcode == Opcode.ADD.value and i + 3 < len(input_dict):
            first_value = get_value(first_mode, input_dict, i, relative_base, 1)
            second_value = get_value(second_mode, input_dict, i, relative_base, 2)
            replace_position = get_replace_position(third_mode, input_dict, i, relative_base, 3)
            input_dict[replace_position] = first_value + second_value
            step = 3

        elif opcode == Opcode.MULTIPLY.value and i + 3 < len(input_dict):
            first_value = get_value(first_mode, input_dict, i, relative_base, 1)
            second_value = get_value(second_mode, input_dict, i, relative_base, 2)
            replace_position = get_replace_position(third_mode, input_dict, i, relative_base, 3)
            input_dict[replace_position] = first_value * second_value
            step = 3

        elif opcode == Opcode.INPUT.value:
            replace_position = get_replace_position(first_mode, input_dict, i, relative_base, 1)
            input_dict[replace_position] = list_of_input_integers[0]
            print("input_value = " + str(list_of_input_integers[0]))
            list_of_input_integers.pop(0)
            step = 1

        elif opcode == Opcode.OUTPUT.value:
            output_value = get_value(first_mode, input_dict, i, relative_base, 1)
            print("output_value = " + str(output_value))
            step = 1

        elif opcode == Opcode.JUMP_IF_TRUE.value:
            step = 2
            first_value = get_value(first_mode, input_dict, i, relative_base, 1)
            if first_value != 0:
                second_value = get_value(second_mode, input_dict, i, relative_base, 2)
                i = second_value
                should_increase_i = False

        elif opcode == Opcode.JUMP_IF_FALSE.value:
            step = 2
            first_value = get_value(first_mode, input_dict, i, relative_base, 1)
            if first_value == 0:
                second_value = get_value(second_mode, input_dict, i, relative_base, 2)
                i = second_value
                should_increase_i = False

        elif opcode == Opcode.LESS_THAN.value:
            first_value = get_value(first_mode, input_dict, i, relative_base, 1)
            second_value = get_value(second_mode, input_dict, i, relative_base, 2)
            place_to_store = get_replace_position(third_mode, input_dict, i, relative_base, 3)

            if first_value < second_value:
                input_dict[place_to_store] = 1
            else:
                input_dict[place_to_store] = 0
            step = 3

        elif opcode == Opcode.EQUALS.value:
            first_value = get_value(first_mode, input_dict, i, relative_base, 1)
            second_value = get_value(second_mode, input_dict, i, relative_base, 2)
            place_to_store = get_replace_position(third_mode, input_dict, i, relative_base, 3)

            if first_value == second_value:
                input_dict[place_to_store] = 1
            else:
                input_dict[place_to_store] = 0
            step = 3

        elif opcode == Opcode.RELATIVE_BASE.value:
            first_value = get_value(first_mode, input_dict, i, relative_base, 1)
            relative_base += first_value
            step = 1

        elif opcode == Opcode.HALT.value:
            break

        if should_increase_i:
            i += step + 1
    return output_value


def get_solution_1():
    return get_output([1], get_dict_of_int_input())


def get_solution_2():
    return get_output([2], get_dict_of_int_input())


if __name__ == "__main__":
    print(get_solution_1())
    print(get_solution_2())
