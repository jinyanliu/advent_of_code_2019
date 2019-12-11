"""
Created at 2019-12-11 19:04

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


class PaintRobotDirection(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


class DirectionValue(Enum):
    LEFT = 0
    RIGHT = 1


class Color(Enum):
    BLACK = 0
    WHITE = 1


def get_dict_of_int_input():
    dict_of_int_input = {}
    i = 0
    with open("day_11_input") as lines:
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


def get_end_location_and_direction(direction_indicator, start_location, start_direction):
    startx, starty = start_location
    end_location, end_direction = start_location, start_direction
    if direction_indicator == DirectionValue.LEFT.value:
        if start_direction == PaintRobotDirection.UP.value:
            end_location = (startx - 1, starty)
            end_direction = PaintRobotDirection.LEFT.value
        elif start_direction == PaintRobotDirection.LEFT.value:
            end_location = (startx, starty - 1)
            end_direction = PaintRobotDirection.DOWN.value
        elif start_direction == PaintRobotDirection.DOWN.value:
            end_location = (startx + 1, starty)
            end_direction = PaintRobotDirection.RIGHT.value
        elif start_direction == PaintRobotDirection.RIGHT.value:
            end_location = (startx, starty + 1)
            end_direction = PaintRobotDirection.UP.value
    elif direction_indicator == DirectionValue.RIGHT.value:
        if start_direction == PaintRobotDirection.UP.value:
            end_location = (startx + 1, starty)
            end_direction = PaintRobotDirection.RIGHT.value
        elif start_direction == PaintRobotDirection.RIGHT.value:
            end_location = (startx, starty - 1)
            end_direction = PaintRobotDirection.DOWN.value
        elif start_direction == PaintRobotDirection.DOWN.value:
            end_location = (startx - 1, starty)
            end_direction = PaintRobotDirection.LEFT.value
        elif start_direction == PaintRobotDirection.LEFT.value:
            end_location = (startx, starty + 1)
            end_direction = PaintRobotDirection.UP.value
    return end_location, end_direction


def get_unique_painted_locations_count(input_dict):
    i = 0
    step = 0
    relative_base = 0
    one_time_output_value = []
    current_location = (0, 0)
    current_direction = PaintRobotDirection.UP.value
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

            input_value = Color.BLACK.value
            if current_location in dict_of_paint_on_location.keys():
                input_value = dict_of_paint_on_location[current_location]

            replace_position = get_replace_position(first_mode, input_dict, i, relative_base, 1)
            input_dict[replace_position] = input_value
            print("input_value = " + str(input_value))

            step = 1

        elif opcode == Opcode.OUTPUT.value:
            output_value = get_value(first_mode, input_dict, i, relative_base, 1)
            print("output_value = " + str(output_value))

            one_time_output_value.append(output_value)
            if len(one_time_output_value) == 2:
                print("output_value_list = " + str(one_time_output_value))
                dict_of_paint_on_location[current_location] = one_time_output_value[0]
                current_location, current_direction = get_end_location_and_direction(one_time_output_value[1],
                                                                                     current_location,
                                                                                     current_direction)
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
    return len(dict_of_paint_on_location.keys())


def get_solution_1():
    return get_unique_painted_locations_count(get_dict_of_int_input())


if __name__ == "__main__":
    print(get_solution_1())
