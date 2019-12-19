"""
Created at 2019-12-19 11:42

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


class DroneState(Enum):
    STATIONARY = 0
    PULLED = 1


def get_dict_of_int_input():
    dict_of_int_input = {}
    i = 0
    with open("day_19_input") as lines:
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


def get_drone_state(input_list, input_dict):
    i = 0
    step = 0
    relative_base = 0
    output_value = 0
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

            input_value = input_list[0]
            input_list.pop(0)
            replace_position = get_replace_position(first_mode, input_dict, i, relative_base, 1)
            input_dict[replace_position] = input_value
            # print("input_value = " + str(input_value))

            step = 1

        elif opcode == Opcode.OUTPUT.value:
            output_value = get_value(first_mode, input_dict, i, relative_base, 1)
            # print("output_value = " + str(output_value))
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

    return output_value


def get_coordinates_list():
    input_list = []
    for x in range(0, 50):
        for y in range(0, 50):
            input_list.append((x, y))
    return input_list


def get_solution_1():
    coordinates_list = get_coordinates_list()
    count_of_state_pulled = 0
    list_of_tuple = []
    for co in coordinates_list:
        x, y = co
        if get_drone_state([x, y], get_dict_of_int_input()) == DroneState.PULLED.value:
            count_of_state_pulled += 1
            list_of_tuple.append((x, y))
    # print(sorted(list_of_tuple, key=lambda x: x[1]))
    return count_of_state_pulled


def get_solution_2():
    list_of_tuple = []
    y = 4
    start_x = 3
    should_stopy = False

    while not should_stopy:
        x = start_x
        should_stopx = False

        while not should_stopx:
            if get_drone_state([x, y], get_dict_of_int_input()) == DroneState.STATIONARY.value:
                last_pulled_inline = (x - 1, y)
                list_of_tuple.append(last_pulled_inline)

                start_x = x

                if (x - 1 - 99 > 0
                        and get_drone_state([x - 1 - 99, y], get_dict_of_int_input()) == DroneState.PULLED.value
                        and get_drone_state([x - 1 - 99, y + 99], get_dict_of_int_input()) == DroneState.PULLED.value
                        and get_drone_state([x - 1, y + 99], get_dict_of_int_input()) == DroneState.PULLED.value):
                    print("found!!!!!" + str(x - 1 - 99) + "," + str(y))
                    should_stopy = True
                    break
                should_stopx = True
            x += 1
        y += 1
        # print(list_of_tuple)
        print(y)
    return (x - 1 - 99) * 10000 + (y - 1)


if __name__ == "__main__":
    print(get_solution_1())
    # The trick point is you cannot investigate it using the example in task explanation.
    # You have to print out your tuple list from solution 1, to see the pattern of your list.
    # The pattern of the example and your list aren't the same !!!!
    # That's my list: [(0, 0), (3, 4), (4, 5), (5, 6), (5, 7), (6, 7), (6, 8), (7, 9), (8, 10), (8, 11), (9, 11), (9, 12), (10, 12), (10, 13), (11, 13), (10, 14), (11, 14), (12, 14), (11, 15), (12, 15), (12, 16), (13, 16), (13, 17), (14, 17), (13, 18), (14, 18), (15, 18), (14, 19), (15, 19), (16, 19), (15, 20), (16, 20), (17, 20), (15, 21), (16, 21), (17, 21), (18, 21), (16, 22), (17, 22), (18, 22), (19, 22), (17, 23), (18, 23), (19, 23), (18, 24), (19, 24), (20, 24), (18, 25), (19, 25), (20, 25), (21, 25), (19, 26), (20, 26), (21, 26), (22, 26), (20, 27), (21, 27), (22, 27), (23, 27), (20, 28), (21, 28), (22, 28), (23, 28), (24, 28), (21, 29), (22, 29), (23, 29), (24, 29), (25, 29), (22, 30), (23, 30), (24, 30), (25, 30), (22, 31), (23, 31), (24, 31), (25, 31), (26, 31), (23, 32), (24, 32), (25, 32), (26, 32), (27, 32), (24, 33), (25, 33), (26, 33), (27, 33), (28, 33), (25, 34), (26, 34), (27, 34), (28, 34), (29, 34), (25, 35), (26, 35), (27, 35), (28, 35), (29, 35), (30, 35), (26, 36), (27, 36), (28, 36), (29, 36), (30, 36), (31, 36), (27, 37), (28, 37), (29, 37), (30, 37), (31, 37), (32, 37), (27, 38), (28, 38), (29, 38), (30, 38), (31, 38), (32, 38), (28, 39), (29, 39), (30, 39), (31, 39), (32, 39), (33, 39), (29, 40), (30, 40), (31, 40), (32, 40), (33, 40), (34, 40), (30, 41), (31, 41), (32, 41), (33, 41), (34, 41), (35, 41), (30, 42), (31, 42), (32, 42), (33, 42), (34, 42), (35, 42), (36, 42), (31, 43), (32, 43), (33, 43), (34, 43), (35, 43), (36, 43), (37, 43), (32, 44), (33, 44), (34, 44), (35, 44), (36, 44), (37, 44), (38, 44), (32, 45), (33, 45), (34, 45), (35, 45), (36, 45), (37, 45), (38, 45), (33, 46), (34, 46), (35, 46), (36, 46), (37, 46), (38, 46), (39, 46), (34, 47), (35, 47), (36, 47), (37, 47), (38, 47), (39, 47), (40, 47), (35, 48), (36, 48), (37, 48), (38, 48), (39, 48), (40, 48), (41, 48), (35, 49), (36, 49), (37, 49), (38, 49), (39, 49), (40, 49), (41, 49), (42, 49)]
    # The trick point is: Not every row has #!!!!! So I have to start from (3,4)
    print(get_solution_2())
