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


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class OutputStatus(Enum):
    SCAFFOLD = 35
    OPEN_SPACE = 46
    NEW_LINE = 10
    UP_SIGN = 94
    DOWN_SIGN = 118


def get_dict_of_int_input():
    dict_of_int_input = {}
    i = 0
    with open("day_17_input_part_2") as lines:
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
        return input_dict[relative_position] if relative_position in input_dict.keys() else 0


def get_replace_position(mode, input_dict, i, relative_base, number):
    if mode == ParametersMode.POSITION.value:
        return input_dict[i + number]
    elif mode == ParametersMode.RELATIVE.value:
        return relative_base + input_dict[i + number]


def plot_message(dict_of_paint_on_location):
    list_of_scaffold = []
    list_of_open_space = []
    list_of_removed = []
    list_of_up_signal = []
    list_of_down_signal = []

    for key, value in dict_of_paint_on_location.items():
        if value == "sca":
            list_of_scaffold.append(key)
        if value == "open":
            list_of_open_space.append(key)
        if value == "removed":
            list_of_removed.append(key)
        if value == "up_signal":
            list_of_up_signal.append(key)
        if value == "down_signal":
            list_of_down_signal.append(key)

    if len(list_of_open_space) > 0:
        g, h = zip(*list_of_open_space)
        matplotlib.pyplot.scatter(g, h, c='pink', marker="4", s=20)

    if len(list_of_scaffold) > 0:
        i, j = zip(*list_of_scaffold)
        matplotlib.pyplot.scatter(i, j, c='black', marker="s", s=20)

    if len(list_of_removed) > 0:
        k, l = zip(*list_of_removed)
        matplotlib.pyplot.scatter(k, l, c='red', marker="o", s=20)

    if len(list_of_up_signal) > 0:
        a, b = zip(*list_of_up_signal)
        matplotlib.pyplot.scatter(a, b, c='blue', marker="^", s=20)

    if len(list_of_down_signal) > 0:
        d, c = zip(*list_of_down_signal)
        matplotlib.pyplot.scatter(d, c, c='blue', marker="v", s=20)

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


def get_alignment_parameters_sum(input_list, input_dict):
    i = 0
    step = 0
    relative_base = 0
    current_location = (-1, 0)
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

            # input_value = 0
            input_value = input_list[0]
            print("input_value = " + str(input_value))
            input_list.pop(0)

            replace_position = get_replace_position(first_mode, input_dict, i, relative_base, 1)
            input_dict[replace_position] = input_value

            step = 1

        elif opcode == Opcode.OUTPUT.value:
            output_value = get_value(first_mode, input_dict, i, relative_base, 1)

            print(chr(output_value), end='')

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
                current_location = (-1, current_y - 1)
                # plot_message(dict_of_paint_on_location)

            elif output_value == OutputStatus.UP_SIGN.value:
                current_x, current_y = current_location
                current_location = (current_x + 1, current_y)
                dict_of_paint_on_location[current_location] = "up_signal"

            elif output_value == OutputStatus.DOWN_SIGN.value:
                current_x, current_y = current_location
                current_location = (current_x + 1, current_y)
                dict_of_paint_on_location[current_location] = "down_signal"

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

    list_of_intersection = []

    for key, value in dict_of_paint_on_location.items():
        if value == "sca":
            keyx, keyy = key

            if ((keyx, keyy + 1) in dict_of_paint_on_location.keys() and dict_of_paint_on_location[
                (keyx, keyy + 1)] == "sca"
                    and (keyx + 1, keyy) in dict_of_paint_on_location.keys() and dict_of_paint_on_location[
                        (keyx + 1, keyy)] == "sca"
                    and (keyx, keyy - 1) in dict_of_paint_on_location.keys() and dict_of_paint_on_location[
                        (keyx, keyy - 1)] == "sca"
                    and (keyx - 1, keyy) in dict_of_paint_on_location.keys() and dict_of_paint_on_location[
                        (keyx - 1, keyy)] == "sca"):
                list_of_intersection.append(key)

    print("intersection:" + str(list_of_intersection))

    result = 0
    for item in list_of_intersection:
        itemx, itemy = item

        # I start to draw at (1,0), not (0,0). That's why the distance to left should - 1
        result += abs(itemx - 1) * abs(itemy)

    list_of_sca = []
    for key, value in dict_of_paint_on_location.items():
        if value == "sca":
            list_of_sca.append(key)

    print(list_of_sca)

    print(list_of_sca[-1])

    start_location = (22, -42)
    end_locaion = (36, -34)
    current_location = start_location
    current_direction = Direction.UP.value
    final_string = ""
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0

    while True:

        if current_location == end_locaion:
            if count_1 != 0:
                final_string += str(count_1) + ", "
            if count_2 != 0:
                final_string += str(count_2) + ", "
            if count_3 != 0:
                final_string += str(count_3) + ", "
            if count_4 != 0:
                final_string += str(count_4) + ", "

        currentx, currenty = current_location
        if current_location != start_location and current_location not in list_of_intersection:
            list_of_sca.remove(current_location)
            dict_of_paint_on_location[current_location] = "removed"
        line_L = "L"
        line_R = "R"

        if current_direction == Direction.UP.value:

            if (currentx, currenty + 1) in list_of_sca:
                if count_1 != 0:
                    final_string += str(count_1) + ", "
                if count_3 != 0:
                    final_string += str(count_3) + ", "
                if count_4 != 0:
                    final_string += str(count_4) + ", "

                count_1 = count_3 = count_4 = 0

                if current_direction == Direction.LEFT.value:
                    final_string += line_R
                    current_direction = Direction.UP.value
                elif current_direction == Direction.RIGHT.value:
                    final_string += line_L
                    current_direction = Direction.UP.value

                count_2 += 1

                current_location = (currentx, currenty + 1)

            elif (currentx + 1, currenty) in list_of_sca:
                if count_1 != 0:
                    final_string += str(count_1) + ", "
                if count_2 != 0:
                    final_string += str(count_2) + ", "
                if count_3 != 0:
                    final_string += str(count_3) + ", "

                count_1 = count_2 = count_3 = 0

                if current_direction == Direction.UP.value:
                    final_string += line_R
                    current_direction = Direction.RIGHT.value
                elif current_direction == Direction.DOWN.value:
                    final_string += line_L
                    current_direction = Direction.RIGHT.value

                count_4 += 1

                current_location = (currentx + 1, currenty)

            elif (currentx, currenty - 1) in list_of_sca:
                if count_1 != 0:
                    final_string += str(count_1) + ", "
                if count_2 != 0:
                    final_string += str(count_2) + ", "
                if count_4 != 0:
                    final_string += str(count_4) + ", "

                count_1 = count_2 = count_4 = 0

                if current_direction == Direction.LEFT.value:
                    final_string += line_L
                    current_direction = Direction.DOWN.value
                elif current_direction == Direction.RIGHT.value:
                    final_string += line_R
                    current_direction = Direction.DOWN.value

                count_3 += 1

                current_location = (currentx, currenty - 1)

            elif (currentx - 1, currenty) in list_of_sca:
                if count_2 != 0:
                    final_string += str(count_2) + ", "
                if count_3 != 0:
                    final_string += str(count_3) + ", "
                if count_4 != 0:
                    final_string += str(count_4) + ", "

                count_2 = count_3 = count_4 = 0

                if current_direction == Direction.UP.value:
                    final_string += line_L
                    current_direction = Direction.LEFT.value
                elif current_direction == Direction.DOWN.value:
                    final_string += line_R
                    current_direction = Direction.LEFT.value

                count_1 += 1

                current_location = (currentx - 1, currenty)
            else:
                break

        elif current_direction == Direction.DOWN.value:

            if (currentx, currenty - 1) in list_of_sca:
                if count_1 != 0:
                    final_string += str(count_1) + ", "
                if count_2 != 0:
                    final_string += str(count_2) + ", "
                if count_4 != 0:
                    final_string += str(count_4) + ", "

                count_1 = count_2 = count_4 = 0

                if current_direction == Direction.LEFT.value:
                    final_string += line_L
                    current_direction = Direction.DOWN.value
                elif current_direction == Direction.RIGHT.value:
                    final_string += line_R
                    current_direction = Direction.DOWN.value

                count_3 += 1

                current_location = (currentx, currenty - 1)

            elif (currentx - 1, currenty) in list_of_sca:
                if count_2 != 0:
                    final_string += str(count_2) + ", "
                if count_3 != 0:
                    final_string += str(count_3) + ", "
                if count_4 != 0:
                    final_string += str(count_4) + ", "

                count_2 = count_3 = count_4 = 0

                if current_direction == Direction.UP.value:
                    final_string += line_L
                    current_direction = Direction.LEFT.value
                elif current_direction == Direction.DOWN.value:
                    final_string += line_R
                    current_direction = Direction.LEFT.value

                count_1 += 1

                current_location = (currentx - 1, currenty)

            elif (currentx, currenty + 1) in list_of_sca:
                if count_1 != 0:
                    final_string += str(count_1) + ", "
                if count_3 != 0:
                    final_string += str(count_3) + ", "
                if count_4 != 0:
                    final_string += str(count_4) + ", "

                count_1 = count_3 = count_4 = 0

                if current_direction == Direction.LEFT.value:
                    final_string += line_R
                    current_direction = Direction.UP.value
                elif current_direction == Direction.RIGHT.value:
                    final_string += line_L
                    current_direction = Direction.UP.value

                count_2 += 1

                current_location = (currentx, currenty + 1)

            elif (currentx + 1, currenty) in list_of_sca:
                if count_1 != 0:
                    final_string += str(count_1) + ", "
                if count_2 != 0:
                    final_string += str(count_2) + ", "
                if count_3 != 0:
                    final_string += str(count_3) + ", "

                count_1 = count_2 = count_3 = 0

                if current_direction == Direction.UP.value:
                    final_string += line_R
                    current_direction = Direction.RIGHT.value
                elif current_direction == Direction.DOWN.value:
                    final_string += line_L
                    current_direction = Direction.RIGHT.value

                count_4 += 1

                current_location = (currentx + 1, currenty)
            else:
                break

        elif current_direction == Direction.RIGHT.value:

            if (currentx + 1, currenty) in list_of_sca:
                if count_1 != 0:
                    final_string += str(count_1) + ", "
                if count_2 != 0:
                    final_string += str(count_2) + ", "
                if count_3 != 0:
                    final_string += str(count_3) + ", "

                count_1 = count_2 = count_3 = 0

                if current_direction == Direction.UP.value:
                    final_string += line_R
                    current_direction = Direction.RIGHT.value
                elif current_direction == Direction.DOWN.value:
                    final_string += line_L
                    current_direction = Direction.RIGHT.value

                count_4 += 1

                current_location = (currentx + 1, currenty)

            elif (currentx, currenty - 1) in list_of_sca:
                if count_1 != 0:
                    final_string += str(count_1) + ", "
                if count_2 != 0:
                    final_string += str(count_2) + ", "
                if count_4 != 0:
                    final_string += str(count_4) + ", "

                count_1 = count_2 = count_4 = 0

                if current_direction == Direction.LEFT.value:
                    final_string += line_L
                    current_direction = Direction.DOWN.value
                elif current_direction == Direction.RIGHT.value:
                    final_string += line_R
                    current_direction = Direction.DOWN.value

                count_3 += 1

                current_location = (currentx, currenty - 1)

            elif (currentx - 1, currenty) in list_of_sca:
                if count_2 != 0:
                    final_string += str(count_2) + ", "
                if count_3 != 0:
                    final_string += str(count_3) + ", "
                if count_4 != 0:
                    final_string += str(count_4) + ", "

                count_2 = count_3 = count_4 = 0

                if current_direction == Direction.UP.value:
                    final_string += line_L
                    current_direction = Direction.LEFT.value
                elif current_direction == Direction.DOWN.value:
                    final_string += line_R
                    current_direction = Direction.LEFT.value

                count_1 += 1

                current_location = (currentx - 1, currenty)

            elif (currentx, currenty + 1) in list_of_sca:
                if count_1 != 0:
                    final_string += str(count_1) + ", "
                if count_3 != 0:
                    final_string += str(count_3) + ", "
                if count_4 != 0:
                    final_string += str(count_4) + ", "

                count_1 = count_3 = count_4 = 0

                if current_direction == Direction.LEFT.value:
                    final_string += line_R
                    current_direction = Direction.UP.value
                elif current_direction == Direction.RIGHT.value:
                    final_string += line_L
                    current_direction = Direction.UP.value

                count_2 += 1

                current_location = (currentx, currenty + 1)

            else:
                break

        elif current_direction == Direction.LEFT.value:

            if (currentx - 1, currenty) in list_of_sca:
                if count_2 != 0:
                    final_string += str(count_2) + ", "
                if count_3 != 0:
                    final_string += str(count_3) + ", "
                if count_4 != 0:
                    final_string += str(count_4) + ", "

                count_2 = count_3 = count_4 = 0

                if current_direction == Direction.UP.value:
                    final_string += line_L
                    current_direction = Direction.LEFT.value
                elif current_direction == Direction.DOWN.value:
                    final_string += line_R
                    current_direction = Direction.LEFT.value

                count_1 += 1

                current_location = (currentx - 1, currenty)

            elif (currentx, currenty + 1) in list_of_sca:
                if count_1 != 0:
                    final_string += str(count_1) + ", "
                if count_3 != 0:
                    final_string += str(count_3) + ", "
                if count_4 != 0:
                    final_string += str(count_4) + ", "

                count_1 = count_3 = count_4 = 0

                if current_direction == Direction.LEFT.value:
                    final_string += line_R
                    current_direction = Direction.UP.value
                elif current_direction == Direction.RIGHT.value:
                    final_string += line_L
                    current_direction = Direction.UP.value

                count_2 += 1

                current_location = (currentx, currenty + 1)

            elif (currentx + 1, currenty) in list_of_sca:
                if count_1 != 0:
                    final_string += str(count_1) + ", "
                if count_2 != 0:
                    final_string += str(count_2) + ", "
                if count_3 != 0:
                    final_string += str(count_3) + ", "

                count_1 = count_2 = count_3 = 0

                if current_direction == Direction.UP.value:
                    final_string += line_R
                    current_direction = Direction.RIGHT.value
                elif current_direction == Direction.DOWN.value:
                    final_string += line_L
                    current_direction = Direction.RIGHT.value

                count_4 += 1

                current_location = (currentx + 1, currenty)

            elif (currentx, currenty - 1) in list_of_sca:
                if count_1 != 0:
                    final_string += str(count_1) + ", "
                if count_2 != 0:
                    final_string += str(count_2) + ", "
                if count_4 != 0:
                    final_string += str(count_4) + ", "

                count_1 = count_2 = count_4 = 0

                if current_direction == Direction.LEFT.value:
                    final_string += line_L
                    current_direction = Direction.DOWN.value
                elif current_direction == Direction.RIGHT.value:
                    final_string += line_R
                    current_direction = Direction.DOWN.value

                count_3 += 1

                current_location = (currentx, currenty - 1)

            else:
                break

        #plot_message(dict_of_paint_on_location)
    print(final_string)

    return output_value


def convert_main_routine():
    target_string = "A,B,A,B,A,C,B,C,A,C"
    new_int_list = []
    for s in target_string:
        new_int_list.append(ord(s))
    new_int_list.append(10)
    print(new_int_list)
    return new_int_list


def convert_a():
    target_string = "L,6,R,12,L,6"
    new_int_list = []
    for s in target_string:
        new_int_list.append(ord(s))
    new_int_list.append(10)
    print(new_int_list)
    return new_int_list


def convert_b():
    target_string = "R,12,L,10,L,4,L,6"
    new_int_list = []
    for s in target_string:
        new_int_list.append(ord(s))
    new_int_list.append(10)
    print(new_int_list)
    return new_int_list


def convert_c():
    target_string = "L,10,L,10,L,4,L,6"
    new_int_list = []
    for s in target_string:
        new_int_list.append(ord(s))
    new_int_list.append(10)
    print(new_int_list)
    return new_int_list


def get_solution_1():
    return get_alignment_parameters_sum(get_dict_of_int_input())


if __name__ == "__main__":
    # print(get_solution_1())
    convert_main_routine()
    convert_a()
    convert_b()
    convert_c()
    last_line = [ord("y"), 10]

    input_list = convert_main_routine() + convert_a() + convert_b() + convert_c() + last_line
    print("input_list=" + str(input_list))

    print(get_alignment_parameters_sum(input_list, get_dict_of_int_input()))
