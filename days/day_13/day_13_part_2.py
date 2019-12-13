"""
Created at 2019-12-13 19:32

@author: jinyanliu
"""
from enum import Enum
import matplotlib.pyplot


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


class PaintRobotDirection(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


class Drawing(Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    HORIZONTAL_PADDLE = 3
    BALL = 4


def get_dict_of_int_input():
    dict_of_int_input = {}
    i = 0
    with open("day_13_input_2") as lines:
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


def get_block_count(input_dict):
    i = 0
    step = 0
    relative_base = 0
    one_time_output_value = []
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
            for key, value in dict_of_paint_on_location.items():
                if value == Drawing.HORIZONTAL_PADDLE.value:
                    horizontal_paddle_location_x, horizontal_paddle_location_y = key
                if value == Drawing.BALL.value:
                    ball_location_x, ball_location_y = key

            if horizontal_paddle_location_x > ball_location_x:
                input_value = -1
            elif horizontal_paddle_location_x < ball_location_x:
                input_value = 1
            else:
                input_value = 0

            replace_position = get_replace_position(first_mode, input_dict, i, relative_base, 1)
            input_dict[replace_position] = input_value
            print("input_value = " + str(input_value))

            step = 1

        elif opcode == Opcode.OUTPUT.value:
            output_value = get_value(first_mode, input_dict, i, relative_base, 1)
            print("output_value = " + str(output_value))

            one_time_output_value.append(output_value)
            if len(one_time_output_value) == 3:
                print("output_value_list = " + str(one_time_output_value))
                x = one_time_output_value[0]
                y = one_time_output_value[1]
                drawing_or_score = one_time_output_value[2]
                if x == -1 and y == 0:
                    print("Current Score is=" + str(drawing_or_score))
                else:
                    dict_of_paint_on_location[(x, -y)] = drawing_or_score
                one_time_output_value = []

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

    plot_message(dict_of_paint_on_location)

    print(dict_of_paint_on_location)

    count_block = 0
    for value in dict_of_paint_on_location.values():
        if value == Drawing.BLOCK.value:
            count_block += 1
    return count_block


def plot_message(dict_of_paint_on_location):
    list_of_empty = []
    list_of_wall = []
    list_of_block = []
    list_of_horizontal_paddle = []
    list_of_ball = []

    for key, value in dict_of_paint_on_location.items():
        if value == Drawing.EMPTY.value:
            list_of_empty.append(key)
        if value == Drawing.WALL.value:
            list_of_wall.append(key)
        if value == Drawing.BLOCK.value:
            list_of_block.append(key)
        if value == Drawing.HORIZONTAL_PADDLE.value:
            list_of_horizontal_paddle.append(key)
        if value == Drawing.BALL.value:
            list_of_ball.append(key)

    if len(list_of_block) > 0:
        a, b = zip(*list_of_block)
        matplotlib.pyplot.scatter(a, b, c='gray', marker="X", s=20)

    if len(list_of_horizontal_paddle) > 0:
        c, d = zip(*list_of_horizontal_paddle)
        matplotlib.pyplot.scatter(c, d, c='green', marker="_", s=20)

    if len(list_of_ball) > 0:
        e, f = zip(*list_of_ball)
        matplotlib.pyplot.scatter(e, f, c='red', marker="8", s=20)

    if len(list_of_empty) > 0:
        g, h = zip(*list_of_empty)
        matplotlib.pyplot.scatter(g, h, c='pink', marker="4", s=20)

    if len(list_of_wall) > 0:
        i, j = zip(*list_of_wall)
        matplotlib.pyplot.scatter(i, j, c='black', marker="s", s=20)

    matplotlib.pyplot.show()


def get_solution_1():
    return get_block_count(get_dict_of_int_input())


if __name__ == "__main__":
    print(get_solution_1())
