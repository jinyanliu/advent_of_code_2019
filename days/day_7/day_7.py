"""
Created at 2019-12-05 19:52

@author: jinyanliu
"""
import itertools
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
    with open("day_7_input") as lines:
        list_of_string = lines.readline().split(',')
        list_of_int = [int(s) for s in list_of_string]
    return list_of_int


def get_dict_instruction(digits):
    instruction_dict = {}
    if len(str(digits)) > 5:
        print("Opcode more than 5 digits: " + str(digits))

    if len(str(digits)) == 5:
        instruction_dict[InstructionDictKey.OPCODE.value] = int(str(digits)[3] + str(digits)[4])
        instruction_dict[InstructionDictKey.FIRST_MODE.value] = int(str(digits)[2])
        instruction_dict[InstructionDictKey.SECOND_MODE.value] = int(str(digits)[1])
        instruction_dict[InstructionDictKey.THIRD_MODE.value] = int(str(digits)[0])

    elif len(str(digits)) == 4:
        instruction_dict[InstructionDictKey.OPCODE.value] = int(str(digits)[2] + str(digits)[3])
        instruction_dict[InstructionDictKey.FIRST_MODE.value] = int(str(digits)[1])
        instruction_dict[InstructionDictKey.SECOND_MODE.value] = int(str(digits)[0])
        instruction_dict[InstructionDictKey.THIRD_MODE.value] = 0

    elif len(str(digits)) == 3:
        instruction_dict[InstructionDictKey.OPCODE.value] = int(str(digits)[1] + str(digits)[2])
        instruction_dict[InstructionDictKey.FIRST_MODE.value] = int(str(digits)[0])
        instruction_dict[InstructionDictKey.SECOND_MODE.value] = 0
        instruction_dict[InstructionDictKey.THIRD_MODE.value] = 0

    elif len(str(digits)) == 2:
        instruction_dict[InstructionDictKey.OPCODE.value] = int(str(digits)[0] + str(digits)[1])
        instruction_dict[InstructionDictKey.FIRST_MODE.value] = 0
        instruction_dict[InstructionDictKey.SECOND_MODE.value] = 0
        instruction_dict[InstructionDictKey.THIRD_MODE.value] = 0

    elif len(str(digits)) == 1:
        instruction_dict[InstructionDictKey.OPCODE.value] = digits
        instruction_dict[InstructionDictKey.FIRST_MODE.value] = 0
        instruction_dict[InstructionDictKey.SECOND_MODE.value] = 0
        instruction_dict[InstructionDictKey.THIRD_MODE.value] = 0

    elif len(str(digits)) == 0:
        print("Opcode is empty: " + str(digits))

    return instruction_dict


def get_instructions(instruction_code):
    dict_instruction = get_dict_instruction(instruction_code)
    opcode = dict_instruction[InstructionDictKey.OPCODE.value]
    first_mode = dict_instruction[InstructionDictKey.FIRST_MODE.value]
    second_mode = dict_instruction[InstructionDictKey.SECOND_MODE.value]
    third_mode = dict_instruction[InstructionDictKey.THIRD_MODE.value]
    return opcode, first_mode, second_mode, third_mode


def get_output(list_of_input_integers, input_list):
    i = 0
    step = 0
    output_value = None
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
            input_list[replace_position] = list_of_input_integers[0]
            list_of_input_integers.pop(0)
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


def get_thruster_signal(phase_setting_string):
    ps1, ps2, ps3, ps4, ps5 = list(map(int, phase_setting_string))
    first_output = get_output([ps1, 0], get_list_of_int_input())
    second_output = get_output([ps2, first_output], get_list_of_int_input())
    third_output = get_output([ps3, second_output], get_list_of_int_input())
    fourth_output = get_output([ps4, third_output], get_list_of_int_input())
    fifth_output = get_output([ps5, fourth_output], get_list_of_int_input())
    return fifth_output


def get_solution_1():
    permutation_string_list = list(map("".join, itertools.permutations('01234')))
    return max(list(map(get_thruster_signal, permutation_string_list)))


if __name__ == "__main__":
    print(get_solution_1())
