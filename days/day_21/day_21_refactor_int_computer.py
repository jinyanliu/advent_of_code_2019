"""
Created at 2019-12-23 14:03

@author: jinyanliu
"""
import threading
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


class Drawing(Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    HORIZONTAL_PADDLE = 3
    BALL = 4


def get_dict_of_int_input():
    dict_of_int_input = {}
    i = 0
    with open("day_21_input") as lines:
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


class IntComputer:
    def __init__(self, inputs_dict, thread_name):
        self._is_halted = False
        self._i = 0
        self._step = 0
        self._relative_base = 0
        self._inputs_dict = inputs_dict
        self._inputs_list = []
        self._outputs_list = []
        self._thread_name = thread_name
        self._current_address = 0

    @property
    def inputs_list(self):
        return self._inputs_list

    @inputs_list.setter
    def inputs_list(self, value):
        self._inputs_list = value

    @property
    def outputs_list(self):
        return self._outputs_list

    @outputs_list.setter
    def outputs_list(self, value):
        self._outputs_list = value

    def get_op_and_actions(self):
        return {
            Opcode.ADD.value: self.perform_add,
            Opcode.MULTIPLY.value: self.perform_multiply,
            Opcode.INPUT.value: self.perform_input,
            Opcode.OUTPUT.value: self.perform_output,
            Opcode.JUMP_IF_TRUE.value: self.perform_jump_if_true,
            Opcode.JUMP_IF_FALSE.value: self.perform_jump_if_false,
            Opcode.LESS_THAN.value: self.perform_less_than,
            Opcode.EQUALS.value: self.perform_equals,
            Opcode.RELATIVE_BASE.value: self.perform_relative_base,
            Opcode.HALT.value: self.perform_halt
        }

    def perform_operation(self):
        opcode, first_mode, second_mode, third_mode = get_instructions(self._inputs_dict[self._current_address])
        return self.get_op_and_actions()[opcode](first_mode, second_mode, third_mode)

    def perform_add(self, first_mode, second_mode, third_mode):
        first_value = get_value(first_mode, self._inputs_dict, self._current_address, self._relative_base, 1)
        second_value = get_value(second_mode, self._inputs_dict, self._current_address, self._relative_base, 2)
        replace_position = get_replace_position(third_mode, self._inputs_dict, self._current_address,
                                                self._relative_base, 3)
        self._inputs_dict[replace_position] = first_value + second_value
        self._current_address += 4

    def perform_multiply(self, first_mode, second_mode, third_mode):
        first_value = get_value(first_mode, self._inputs_dict, self._current_address, self._relative_base, 1)
        second_value = get_value(second_mode, self._inputs_dict, self._current_address, self._relative_base, 2)
        replace_position = get_replace_position(third_mode, self._inputs_dict, self._current_address,
                                                self._relative_base, 3)
        self._inputs_dict[replace_position] = first_value * second_value
        self._current_address += 4

    def perform_input(self, first_mode, second_mode, third_mode):
        input_value = self.inputs_list[0]
        self.inputs_list.pop(0)
        replace_position = get_replace_position(first_mode, self._inputs_dict, self._current_address,
                                                self._relative_base, 1)
        self._inputs_dict[replace_position] = input_value
        # print("input_value = " + str(input_value))
        self._current_address += 2

    def perform_output(self, first_mode, second_mode, third_mode):
        output_value = get_value(first_mode, self._inputs_dict, self._current_address, self._relative_base, 1)
        self.outputs_list.append(output_value)
        # print("output_value = " + str(output_value))
        # print(chr(output_value), end='')
        self._current_address += 2

    def perform_jump_if_true(self, first_mode, second_mode, third_mode):
        first_value = get_value(first_mode, self._inputs_dict, self._current_address, self._relative_base, 1)
        if first_value != 0:
            second_value = get_value(second_mode, self._inputs_dict, self._current_address, self._relative_base, 2)
            self._current_address = second_value
        else:
            self._current_address += 3

    def perform_jump_if_false(self, first_mode, second_mode, third_mode):
        first_value = get_value(first_mode, self._inputs_dict, self._current_address, self._relative_base, 1)
        if first_value == 0:
            second_value = get_value(second_mode, self._inputs_dict, self._current_address, self._relative_base, 2)
            self._current_address = second_value
        else:
            self._current_address += 3

    def perform_less_than(self, first_mode, second_mode, third_mode):
        first_value = get_value(first_mode, self._inputs_dict, self._current_address, self._relative_base, 1)
        second_value = get_value(second_mode, self._inputs_dict, self._current_address, self._relative_base, 2)
        place_to_store = get_replace_position(third_mode, self._inputs_dict, self._current_address, self._relative_base,
                                              3)
        if first_value < second_value:
            self._inputs_dict[place_to_store] = 1
        else:
            self._inputs_dict[place_to_store] = 0
        self._current_address += 4

    def perform_equals(self, first_mode, second_mode, third_mode):
        first_value = get_value(first_mode, self._inputs_dict, self._current_address, self._relative_base, 1)
        second_value = get_value(second_mode, self._inputs_dict, self._current_address, self._relative_base, 2)
        place_to_store = get_replace_position(third_mode, self._inputs_dict, self._current_address, self._relative_base,
                                              3)
        if first_value == second_value:
            self._inputs_dict[place_to_store] = 1
        else:
            self._inputs_dict[place_to_store] = 0
        self._current_address += 4

    def perform_relative_base(self, first_mode, second_mode, third_mode):
        first_value = get_value(first_mode, self._inputs_dict, self._current_address, self._relative_base, 1)
        self._relative_base += first_value
        self._current_address += 2

    def perform_halt(self, first_mode, second_mode, third_mode):
        self._is_halted = True

    def run_program(self):
        while not self._is_halted:
            self.perform_operation()


def encode_to_ascii(target_string):
    new_int_list = []
    for s in target_string:
        new_int_list.append(ord(s))
    new_int_list.append(10)
    print(new_int_list)
    return new_int_list


def get_solution_1():
    input_list = []
    # (!A or !B or !C) and D
    list_of_instruction = ["NOT A J",
                           "NOT B T",
                           "OR T J",
                           "NOT C T",
                           "OR T J",
                           "AND D J",
                           "WALK"]
    for item in list_of_instruction:
        input_list += encode_to_ascii(item)
        print("thread 1")

    intComputer = IntComputer(get_dict_of_int_input(), "thread 1")
    intComputer.inputs_list = input_list
    intComputer.run_program()
    return intComputer.outputs_list[-1]


def get_solution_2():
    input_list = []
    # (!A or !B or !C) and D and (E or H)
    # !(!E and !H) and D and !(A and B and C)
    list_of_instruction = ["NOT E T",
                           "NOT H J",
                           "AND T J",
                           "NOT J J",
                           "AND D J",
                           "NOT A T",
                           "NOT T T",
                           "AND B T",
                           "AND C T",
                           "NOT T T",
                           "AND T J",
                           "RUN"]
    for item in list_of_instruction:
        input_list += encode_to_ascii(item)
        print("thread 2")

    intComputer = IntComputer(get_dict_of_int_input(), "thread 2")
    intComputer.inputs_list = input_list
    intComputer.run_program()
    return intComputer.outputs_list[-1]


class myThread(threading.Thread):
    def __init__(self, thread_name, inputs_list):
        threading.Thread.__init__(self)
        self._inputs_list = inputs_list
        self._thread_name = thread_name

    def run(self):
        intComputer = IntComputer(get_dict_of_int_input(), self._thread_name)
        intComputer.inputs_list = self._inputs_list
        intComputer.run_program()
        print(intComputer.outputs_list[-1])


if __name__ == "__main__":
    input_list_1 = []
    # (!A or !B or !C) and D
    list_of_instruction = ["NOT A J",
                           "NOT B T",
                           "OR T J",
                           "NOT C T",
                           "OR T J",
                           "AND D J",
                           "WALK"]
    for item in list_of_instruction:
        input_list_1 += encode_to_ascii(item)

    input_list_2 = []
    # (!A or !B or !C) and D and (E or H)
    # !(!E and !H) and D and !(A and B and C)
    list_of_instruction = ["NOT E T",
                           "NOT H J",
                           "AND T J",
                           "NOT J J",
                           "AND D J",
                           "NOT A T",
                           "NOT T T",
                           "AND B T",
                           "AND C T",
                           "NOT T T",
                           "AND T J",
                           "RUN"]
    for item in list_of_instruction:
        input_list_2 += encode_to_ascii(item)

    # Create new threads
    thread1 = myThread("thread 1", input_list_1)
    thread2 = myThread("thread 2", input_list_2)

    # Start new Threads
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
