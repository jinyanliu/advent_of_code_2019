"""
Created at 2019-12-23 14:01

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


def get_dict_of_int_input():
    dict_of_int_input = {}
    i = 0
    with open("day_23_input") as lines:
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
    def __init__(self, inputs_dict):
        self._is_halted = False
        self._relative_base = 0
        self._inputs_dict = inputs_dict
        self._inputs_list = []
        self._outputs_list = []
        self._current_address = 0

    @property
    def is_halted(self):
        return self._is_halted

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
        if len(self.inputs_list) > 0:
            input_value = self.inputs_list[0]
            self.inputs_list.pop(0)
        else:
            input_value = -1
        replace_position = get_replace_position(first_mode, self._inputs_dict, self._current_address,
                                                self._relative_base, 1)
        self._inputs_dict[replace_position] = input_value
        # print("input_value = " + str(input_value))
        self._current_address += 2

    def perform_output(self, first_mode, second_mode, third_mode):
        output_value = get_value(first_mode, self._inputs_dict, self._current_address, self._relative_base, 1)
        self.outputs_list.append(output_value)
        # print("output_value = " + str(output_value))
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


class Day23:
    def __init__(self):
        self._computers = []

    @property
    def computers(self):
        return self._computers

    def get_inputs_dict(self):
        return get_dict_of_int_input()

    def get_solution_1(self):
        inputs_dict = self.get_inputs_dict()
        for i in range(0, 50):
            computer = IntComputer(inputs_dict.copy())
            computer.inputs_list.append(i)
            self.computers.append(computer)

        for computer in self.computers:
            t = threading.Thread(target=self.run_computer, args=(computer,))
            t.start()

    def run_computer(self, me: IntComputer):
        while not me.is_halted:
            me.perform_operation()

            if len(me.outputs_list) == 3:
                addr = me.outputs_list[0]
                x = me.outputs_list[1]
                y = me.outputs_list[2]
                del me.outputs_list[2]
                del me.outputs_list[1]
                del me.outputs_list[0]

                if addr == 255:
                    print("Address=", addr, ", x=", x, ", y=", y)

                if addr in range(0, 50):
                    self.computers[addr].inputs_list.append(x)
                    self.computers[addr].inputs_list.append(y)


if __name__ == "__main__":
    today = Day23()
    today.get_solution_1()
