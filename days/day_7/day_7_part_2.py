"""
Created at 2019-12-07 13:59

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


def get_output(start_index, list_of_input_integers, input_list):
    i = start_index
    step = 0
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
            print("input_value = " + str(list_of_input_integers[0]))
            list_of_input_integers.pop(0)
            step = 1

        elif opcode == Opcode.OUTPUT.value:
            output_value = input_list[input_list[i + 1]] if (first_mode == ParametersMode.POSITION.value) else \
                input_list[
                    i + 1]
            step = 1
            next_start_position = i + step + 1
            current_list = input_list
            print("output_value = " + str(output_value))
            print("new start position = " + str(i + step + 1))
            print("current_list=" + str(current_list))
            return output_value, next_start_position, current_list

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
            print("halt")
            break

        if should_increase_i:
            i += step + 1


def get_thruster_signal(phase_setting_string):
    ps1, ps2, ps3, ps4, ps5 = list(map(int, phase_setting_string))

    print("\nfirst amlifier starts...")
    amp_a_output, amp_a_next_start_index, amp_a_next_list = get_output(0, [ps1, 0], get_list_of_int_input())

    print("\nsecond amlifier starts...")
    amp_b_output, amp_b_next_start_index, amp_b_next_list = get_output(0, [ps2, amp_a_output], get_list_of_int_input())

    print("\nthird amlifier starts...")
    amp_c_output, amp_c_next_start_index, amp_c_next_list = get_output(0, [ps3, amp_b_output], get_list_of_int_input())

    print("\nfourth amlifier starts...")
    amp_d_output, amp_d_next_start_index, amp_d_next_list = get_output(0, [ps4, amp_c_output], get_list_of_int_input())

    print("\nfifth amlifier starts...")
    amp_e_output, amp_e_next_start_index, amp_e_next_list = get_output(0, [ps5, amp_d_output], get_list_of_int_input())

    while True:
        try:
            print("\nfirst amlifier starts...")
            amp_a_output, amp_a_next_start_index, amp_a_next_list = get_output(amp_a_next_start_index, [amp_e_output],
                                                                               amp_a_next_list)
        except TypeError:
            print("catched")
            return amp_e_output

        print("\nsecond amlifier starts...")
        amp_b_output, amp_b_next_start_index, amp_b_next_list = get_output(amp_b_next_start_index, [amp_a_output],
                                                                           amp_b_next_list)

        if amp_b_output is None:
            return amp_a_output

        print("\nthird amlifier starts...")
        amp_c_output, amp_c_next_start_index, amp_c_next_list = get_output(amp_c_next_start_index, [amp_b_output],
                                                                           amp_c_next_list)

        if amp_c_output is None:
            return amp_b_output

        print("\nfourth amlifier starts...")
        amp_d_output, amp_d_next_start_index, amp_d_next_list = get_output(amp_d_next_start_index, [amp_c_output],
                                                                           amp_d_next_list)

        if amp_d_output is None:
            return amp_c_output

        print("\nfifth amlifier starts...")
        amp_e_output, amp_e_next_start_index, amp_e_next_list = get_output(amp_e_next_start_index, [amp_d_output],
                                                                           amp_e_next_list)

        if amp_e_output is None:
            return amp_d_output


def get_solution_2():
    permutation_string_list = list(map("".join, itertools.permutations('56789')))
    return max(list(map(get_thruster_signal, permutation_string_list)))


if __name__ == "__main__":
    print(get_solution_2())
