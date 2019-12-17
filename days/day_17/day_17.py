"""
Created at 2019-12-17 19:30

@author: jinyanliu
"""
from enum import Enum

import matplotlib
import matplotlib.pyplot as plt


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


# class Direction(Enum):
#     UP = 1
#     DOWN = 2
#     LEFT = 3
#     RIGHT = 4


class OutputStatus(Enum):
    SCAFFOLD = 35
    OPEN_SPACE = 46
    NEW_LINE = 10


def get_dict_of_int_input():
    dict_of_int_input = {}
    i = 0
    with open("day_17_input") as lines:
        list_of_string = lines.readline().split(',')
        for s in list_of_string:
            dict_of_int_input[i] = int(s)
            i += 1
    # print(dict_of_int_input)
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


def plot_message(dict_of_paint_on_location):
    list_of_scaffold = []
    list_of_open_space = []

    for key, value in dict_of_paint_on_location.items():
        if value == "sca":
            list_of_scaffold.append(key)
        if value == "open":
            list_of_open_space.append(key)

    if len(list_of_open_space) > 0:
        g, h = zip(*list_of_open_space)
        matplotlib.pyplot.scatter(g, h, c='pink', marker="4", s=20)

    if len(list_of_scaffold) > 0:
        i, j = zip(*list_of_scaffold)
        matplotlib.pyplot.scatter(i, j, c='black', marker="s", s=20)

    matplotlib.pyplot.show()


# def get_new_location(current_location, current_direction):
#     new_location = (0, 0)
#     current_x, current_y = current_location
#     if current_direction == Direction.UP.value:
#         new_location = (current_x, current_y + 1)
#     elif current_direction == Direction.DOWN.value:
#         new_location = (current_x, current_y - 1)
#     elif current_direction == Direction.LEFT.value:
#         new_location = (current_x - 1, current_y)
#     elif current_direction == Direction.RIGHT.value:
#         new_location = (current_x + 1, current_y)
#     return new_location


# def get_input(current_location, dict_of_paint_on_location):
#     current_x, current_y = current_location
#     up_location = (current_x, current_y + 1)
#     down_location = (current_x, current_y - 1)
#     left_location = (current_x - 1, current_y)
#     right_location = (current_x + 1, current_y)
#     if up_location not in dict_of_paint_on_location.keys():
#         return Direction.UP.value
#     if right_location not in dict_of_paint_on_location.keys():
#         return Direction.RIGHT.value
#     if down_location not in dict_of_paint_on_location.keys():
#         return Direction.DOWN.value
#     if left_location not in dict_of_paint_on_location.keys():
#         return Direction.LEFT.value
#
#     if not dict_of_paint_on_location[up_location] == "wall":
#         return Direction.UP.value
#     if not dict_of_paint_on_location[right_location] == "wall":
#         return Direction.RIGHT.value
#     if not dict_of_paint_on_location[down_location] == "wall":
#         return Direction.DOWN.value
#     if not dict_of_paint_on_location[left_location] == "wall":
#         return Direction.LEFT.value


def get_alignment_parameters_sum(input_dict):
    i = 0
    step = 0
    relative_base = 0
    current_location = (0, 0)
    dict_of_paint_on_location = {}

    while i + 1 < len(input_dict):
        should_increase_i = True

        opcode, first_mode, second_mode, third_mode = get_instructions(input_dict[i])

        if opcode == Opcode.ADD.value:
            first_value = get_value(first_mode, input_dict, i, relative_base, 1)
            second_value = get_value(second_mode, input_dict, i, relative_base, 2)
            replace_position = get_replace_position(third_mode, input_dict, i, relative_base, 3)
            input_dict[replace_position] = first_value + second_value
            step = 3

        elif opcode == Opcode.MULTIPLY.value:
            first_value = get_value(first_mode, input_dict, i, relative_base, 1)
            second_value = get_value(second_mode, input_dict, i, relative_base, 2)
            replace_position = get_replace_position(third_mode, input_dict, i, relative_base, 3)
            input_dict[replace_position] = first_value * second_value
            step = 3

        elif opcode == Opcode.INPUT.value:

            # input_value = get_input(current_location, dict_of_paint_on_location)

            input_value = 0

            current_direction = input_value
            replace_position = get_replace_position(first_mode, input_dict, i, relative_base, 1)
            input_dict[replace_position] = input_value

            step = 1

        elif opcode == Opcode.OUTPUT.value:
            output_value = get_value(first_mode, input_dict, i, relative_base, 1)
            # print("output_value = " + str(output_value))

            if output_value == OutputStatus.SCAFFOLD.value:
                current_x, current_y = current_location
                current_location = (current_x + 1, current_y)
                # print("current_position=" + str(current_location))
                dict_of_paint_on_location[current_location] = "sca"
                # plot_message(dict_of_paint_on_location)

            elif output_value == OutputStatus.OPEN_SPACE.value:
                current_x, current_y = current_location
                current_location = (current_x + 1, current_y)
                # print("current_position=" + str(current_location))
                dict_of_paint_on_location[current_location] = "open"
                # plot_message(dict_of_paint_on_location)

            elif output_value == OutputStatus.NEW_LINE.value:
                # print("current_position=" + str(current_location))
                current_x, current_y = current_location
                current_location = (0, current_y - 1)
                # plot_message(dict_of_paint_on_location)

            # plot_message(dict_of_paint_on_location)

            step = 1

        elif opcode == Opcode.JUMP_IF_TRUE.value:
            first_value = get_value(first_mode, input_dict, i, relative_base, 1)
            if first_value != 0:
                second_value = get_value(second_mode, input_dict, i, relative_base, 2)
                i = second_value
                should_increase_i = False
            step = 2

        elif opcode == Opcode.JUMP_IF_FALSE.value:
            first_value = get_value(first_mode, input_dict, i, relative_base, 1)
            if first_value == 0:
                second_value = get_value(second_mode, input_dict, i, relative_base, 2)
                i = second_value
                should_increase_i = False
            step = 2

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

    print(dict_of_paint_on_location)
    #plot_message(dict_of_paint_on_location)

    list_of_intersection= []

    for key, value in dict_of_paint_on_location.items():
        if value == "sca":
            keyx, keyy = key

            if ((keyx, keyy + 1) in dict_of_paint_on_location.keys() and dict_of_paint_on_location[(keyx, keyy + 1)] == "sca"
                    and (keyx + 1, keyy) in dict_of_paint_on_location.keys() and dict_of_paint_on_location[(keyx + 1, keyy)] == "sca"
                    and (keyx, keyy - 1) in dict_of_paint_on_location.keys() and dict_of_paint_on_location[(keyx, keyy - 1)] == "sca"
                    and (keyx - 1, keyy) in dict_of_paint_on_location.keys() and dict_of_paint_on_location[
                        (keyx - 1, keyy)] == "sca"):
                list_of_intersection.append(key)

    print("intersection:"+str(list_of_intersection))

    result = 0
    for item in list_of_intersection:
        itemx, itemy = item

        # I start to draw at (1,0), not (0,0). That's why the distance to left should - 1
        result += abs(itemx-1)*abs(itemy)

    return result


def get_solution_1():
    return get_alignment_parameters_sum(get_dict_of_int_input())


if __name__ == "__main__":
    print(get_solution_1())
