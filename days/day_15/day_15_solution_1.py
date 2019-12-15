"""
Created at 2019-12-15 14:44

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


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class OutputStatus(Enum):
    WALL = 0
    MOVE = 1
    FOUND = 2


def get_dict_of_int_input():
    dict_of_int_input = {}
    i = 0
    with open("day_15_input") as lines:
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
    list_of_empty = []
    list_of_wall = []
    list_of_start = []
    list_of_current = []
    list_of_target = []

    for key, value in dict_of_paint_on_location.items():
        if value == "wall":
            list_of_wall.append(key)
        if value == "start":
            list_of_start.append(key)
        if value == "empty":
            list_of_empty.append(key)
        if value == "current":
            list_of_empty.append(key)
        if value == "target":
            list_of_target.append(key)

    if len(list_of_start) > 0:
        a, b = zip(*list_of_start)
        matplotlib.pyplot.scatter(a, b, c='gray', marker="X", s=20)

    if len(list_of_empty) > 0:
        g, h = zip(*list_of_empty)
        matplotlib.pyplot.scatter(g, h, c='pink', marker="4", s=20)

    if len(list_of_wall) > 0:
        i, j = zip(*list_of_wall)
        matplotlib.pyplot.scatter(i, j, c='black', marker="s", s=20)

    if len(list_of_current) > 0:
        c, d = zip(*list_of_current)
        matplotlib.pyplot.scatter(c, d, c='red', marker="8", s=20)

    if len(list_of_target) > 0:
        e, f = zip(*list_of_target)
        matplotlib.pyplot.scatter(e, f, c='red', marker="_", s=20)

    matplotlib.pyplot.show()


def get_new_location(current_location, current_direction):
    new_location = (0, 0)
    current_x, current_y = current_location
    if current_direction == Direction.UP.value:
        new_location = (current_x, current_y + 1)
    elif current_direction == Direction.DOWN.value:
        new_location = (current_x, current_y - 1)
    elif current_direction == Direction.LEFT.value:
        new_location = (current_x - 1, current_y)
    elif current_direction == Direction.RIGHT.value:
        new_location = (current_x + 1, current_y)
    return new_location


def get_input(current_location, dict_of_paint_on_location):
    current_x, current_y = current_location
    up_location = (current_x, current_y + 1)
    down_location = (current_x, current_y - 1)
    left_location = (current_x - 1, current_y)
    right_location = (current_x + 1, current_y)
    if up_location not in dict_of_paint_on_location.keys():
        return Direction.UP.value
    if right_location not in dict_of_paint_on_location.keys():
        return Direction.RIGHT.value
    if down_location not in dict_of_paint_on_location.keys():
        return Direction.DOWN.value
    if left_location not in dict_of_paint_on_location.keys():
        return Direction.LEFT.value

    if not dict_of_paint_on_location[up_location] == "wall":
        return Direction.UP.value
    if not dict_of_paint_on_location[right_location] == "wall":
        return Direction.RIGHT.value
    if not dict_of_paint_on_location[down_location] == "wall":
        return Direction.DOWN.value
    if not dict_of_paint_on_location[left_location] == "wall":
        return Direction.LEFT.value


def get_empty_count(input_dict):
    i = 0
    step = 0
    relative_base = 0
    current_direction = 0
    current_location = (0, 0)
    dict_of_paint_on_location = {}
    dict_of_graph_on_location = {}
    dict_of_paint_on_location[current_location] = "start"
    dict_of_graph_on_location[current_location] = "start"
    count_of_input = 0
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
            count_of_input += 1

            input_value = get_input(current_location, dict_of_paint_on_location)

            current_direction = input_value
            replace_position = get_replace_position(first_mode, input_dict, i, relative_base, 1)
            input_dict[replace_position] = input_value

            step = 1

        elif opcode == Opcode.OUTPUT.value:
            output_value = get_value(first_mode, input_dict, i, relative_base, 1)
            #print("output_value = " + str(output_value))

            if output_value == OutputStatus.WALL.value:
                # current location is not changed
                current_location = current_location
                #print("current_position=" + str(current_location))
                wall_location = get_new_location(current_location, current_direction)
                dict_of_paint_on_location[wall_location] = "wall"
                dict_of_graph_on_location[wall_location] = "wall"
                # plot_message(dict_of_paint_on_location)

            elif output_value == OutputStatus.MOVE.value:
                current_location = get_new_location(current_location, current_direction)
                #print("current_position=" + str(current_location))
                dict_of_paint_on_location[current_location] = "empty"
                dict_of_graph_on_location[current_location] = "empty"
                # plot_message(dict_of_paint_on_location)


            elif output_value == OutputStatus.FOUND.value:
                #print("current_position=" + str(current_location))
                current_location = target_location = get_new_location(current_location, current_direction)
                dict_of_paint_on_location[current_location] = "target"
                dict_of_graph_on_location[current_location] = "target"
                # plot_message(dict_of_paint_on_location)
                break

            currentx, currenty = current_location
            if ((currentx, currenty + 1) in dict_of_paint_on_location.keys() and dict_of_paint_on_location[
                (currentx, currenty + 1)] == "wall"
                    and (currentx + 1, currenty) in dict_of_paint_on_location.keys() and dict_of_paint_on_location[
                        (currentx + 1, currenty)] == "wall"
                    and (currentx, currenty - 1) in dict_of_paint_on_location.keys() and dict_of_paint_on_location[
                        (currentx, currenty - 1)] == "wall"):
                dict_of_paint_on_location[current_location] = "wall"

            if ((currentx - 1, currenty) in dict_of_paint_on_location.keys() and dict_of_paint_on_location[
                (currentx - 1, currenty)] == "wall"
                    and (currentx + 1, currenty) in dict_of_paint_on_location.keys() and dict_of_paint_on_location[
                        (currentx + 1, currenty)] == "wall"
                    and (currentx, currenty - 1) in dict_of_paint_on_location.keys() and dict_of_paint_on_location[
                        (currentx, currenty - 1)] == "wall"):
                dict_of_paint_on_location[current_location] = "wall"

            if ((currentx - 1, currenty) in dict_of_paint_on_location.keys() and dict_of_paint_on_location[
                (currentx - 1, currenty)] == "wall"
                    and (currentx, currenty + 1) in dict_of_paint_on_location.keys() and dict_of_paint_on_location[
                        (currentx, currenty + 1)] == "wall"
                    and (currentx, currenty - 1) in dict_of_paint_on_location.keys() and dict_of_paint_on_location[
                        (currentx, currenty - 1)] == "wall"):
                dict_of_paint_on_location[current_location] = "wall"

            if ((currentx - 1, currenty) in dict_of_paint_on_location.keys() and dict_of_paint_on_location[
                (currentx - 1, currenty)] == "wall"
                    and (currentx, currenty + 1) in dict_of_paint_on_location.keys() and dict_of_paint_on_location[
                        (currentx, currenty + 1)] == "wall"
                    and (currentx + 1, currenty) in dict_of_paint_on_location.keys() and dict_of_paint_on_location[
                        (currentx + 1, currenty)] == "wall"):
                dict_of_paint_on_location[current_location] = "wall"

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

    for key, value in dict_of_paint_on_location.items():
        if value == "start":
            # start point has been overwritten as "wall" by me
            print("start location= " + str(key))
        if value == "target":
            print("target location= " + str(key))
    print(dict_of_paint_on_location)
    print("count of input= " + str(count_of_input))

    dict_of_paint_on_location[(0, 0)] = "start"
    dict_of_graph_on_location[(0, 0)] = "start"

    # puzzle graph without customized wall
    plot_message(dict_of_graph_on_location)
    # mine graph with customized wall
    plot_message(dict_of_paint_on_location)

    empty_count = 0
    for key, value in dict_of_paint_on_location.items():
        if value == "empty":
            empty_count += 1

    return empty_count + 2


def get_solution_1():
    return get_empty_count(get_dict_of_int_input())


if __name__ == "__main__":
    print(get_solution_1())
