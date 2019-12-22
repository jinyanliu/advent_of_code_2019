"""
Created at 2019-12-22 12:52

@author: jinyanliu
"""
import collections
from enum import Enum


class Method(Enum):
    DEAL_INTO_NEW_STACK = "deal into new stack"
    DEAL_WITH_INCREMENT = "deal with increment"
    CUT = "cut"


def get_instructions_list():
    instructions_list = []
    with open("day_22_input") as lines:
        for line in lines:
            instructions_list.append(line)
    # print(instructions_list)
    return instructions_list


class ShuffleComputer:
    def __init__(self, start_deck):
        self._current_deck = start_deck

    @property
    def current_deck(self):
        return self._current_deck

    @current_deck.setter
    def current_deck(self, value):
        self._current_deck = value

    def deal_with_increment(self, step):
        deck_len = len(self.current_deck)
        new_deck = {}
        new_deck[0] = self.current_deck[0]
        current_old_deck_position = 0
        current_new_deck_position = 0

        while len(new_deck) < len(self.current_deck):
            if current_new_deck_position + step < deck_len:
                new_deck[current_new_deck_position + step] = self.current_deck[current_old_deck_position + 1]
                current_old_deck_position = current_old_deck_position + 1
                current_new_deck_position = current_new_deck_position + step
            else:
                new_deck[current_new_deck_position + step - (deck_len - 1) - 1] = self.current_deck[
                    current_old_deck_position + 1]
                current_old_deck_position = current_old_deck_position + 1
                current_new_deck_position = current_new_deck_position + step - (deck_len - 1) - 1

        # print(self.current_deck)
        # print(new_deck)
        new_deck = collections.OrderedDict(sorted(new_deck.items()))
        self.current_deck = new_deck

    def deal_into_new_stack(self):
        target_list = []
        new_deck = {}
        for value in self.current_deck.values():
            target_list.append(value)
        target_list.reverse()
        i = 0
        for value in target_list:
            new_deck[i] = value
            i += 1

        # print(new_deck)
        self.current_deck = new_deck

    def cut(self, size):
        target_list = []
        new_deck = {}
        for value in self.current_deck.values():
            target_list.append(value)

        if size >= 0:
            new_list = target_list[size:]
            new_list = new_list + target_list[:size]
        else:
            size = abs(size)
            new_list = target_list[:(len(target_list) - size)]
            new_list = target_list[(len(target_list) - size):] + new_list
        i = 0
        for value in new_list:
            new_deck[i] = value
            i += 1

        # print(new_deck)
        self.current_deck = new_deck

    def get_position_of_card(self, card_number):
        for key, value in self.current_deck.items():
            if card_number == value:
                return key

    def get_instructions_and_actions(self):
        return {
            Method.DEAL_WITH_INCREMENT.value: self.deal_with_increment,
            Method.DEAL_INTO_NEW_STACK.value: self.deal_into_new_stack,
            Method.CUT.value: self.cut
        }


def get_solution_1():
    map_dict = {}
    for i in range(0, 10007):
        map_dict[i] = i

    computer = ShuffleComputer(map_dict)

    for instruction in get_instructions_list():
        if Method.DEAL_WITH_INCREMENT.value in instruction:
            input = [int(s) for s in str.split(instruction) if s.isdigit()][0]
            computer.get_instructions_and_actions()[Method.DEAL_WITH_INCREMENT.value](input)
        elif Method.DEAL_INTO_NEW_STACK.value in instruction:
            computer.get_instructions_and_actions()[Method.DEAL_INTO_NEW_STACK.value]()
        elif Method.CUT.value in instruction:
            input = int(instruction.split(" ")[1])
            computer.get_instructions_and_actions()[Method.CUT.value](input)

    print(computer.current_deck)

    return computer.get_position_of_card(2019)


if __name__ == "__main__":
    print(get_solution_1())
