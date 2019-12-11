"""
Created at 2019-12-10 20:29

@author: jinyanliu
"""
import functools
from enum import Enum
import math


class Step(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8


def get_list_of_input_tuple():
    list_of_input_tuple = []
    with open("day_10_input") as lines:
        y = 0
        for line in lines:
            x = 0
            for char in line:
                if char == '#':
                    list_of_input_tuple.append((x, y))
                x += 1
            y += 1
    return list_of_input_tuple


def get_dict_of_different_angles(base_tuple):
    dict_of_different_angle = {}
    basex, basey = base_tuple
    new_list = get_list_of_input_tuple()[:]
    new_list.remove(base_tuple)
    for tuple in new_list:
        currentx, currenty = tuple
        offsetx, offsety = basex - currentx, basey - currenty
        current_offset_gcd = math.gcd(offsetx, offsety)
        # Here we want to avoid using float. Float is unreliable at comparison.
        keyoffsetx, keyoffsety = offsetx // current_offset_gcd, offsety // current_offset_gcd
        tuple_key = (keyoffsetx, keyoffsety)

        if tuple_key not in dict_of_different_angle.keys():
            dict_of_different_angle[tuple_key] = [(currentx, currenty)]
        else:
            dict_of_different_angle[tuple_key].append((currentx, currenty))
            dict_of_different_angle[tuple_key] = sorted(dict_of_different_angle[tuple_key],
                                                        key=lambda x: abs(basex - x[0]))
            dict_of_different_angle[tuple_key] = sorted(dict_of_different_angle[tuple_key],
                                                        key=lambda x: abs(basey - x[1]))
    return dict_of_different_angle


def get_dict_of_steps(offset_key_of_dict_of_different_angles):
    dict_of_steps = {Step.ONE.value: [], Step.TWO.value: [], Step.THREE.value: [], Step.FOUR.value: [],
                     Step.FIVE.value: [], Step.SIX.value: [], Step.SEVEN.value: [], Step.EIGHT.value: []}

    for offset_key in offset_key_of_dict_of_different_angles:
        offset_key_x, offset_key_y = offset_key

        if offset_key_x == 0 and offset_key_y > 0:
            dict_of_steps[Step.ONE.value].append((offset_key_x, offset_key_y))
        elif offset_key_x < 0 and offset_key_y > 0:
            dict_of_steps[Step.TWO.value].append((offset_key_x, offset_key_y))
        elif offset_key_x < 0 and offset_key_y == 0:
            dict_of_steps[Step.THREE.value].append((offset_key_x, offset_key_y))
        elif offset_key_x < 0 and offset_key_y < 0:
            dict_of_steps[Step.FOUR.value].append((offset_key_x, offset_key_y))
        elif offset_key_x == 0 and offset_key_y < 0:
            dict_of_steps[Step.FIVE.value].append((offset_key_x, offset_key_y))
        elif offset_key_x > 0 and offset_key_y < 0:
            dict_of_steps[Step.SIX.value].append((offset_key_x, offset_key_y))
        elif offset_key_x > 0 and offset_key_y == 0:
            dict_of_steps[Step.SEVEN.value].append((offset_key_x, offset_key_y))
        elif offset_key_x > 0 and offset_key_y > 0:
            dict_of_steps[Step.EIGHT.value].append((offset_key_x, offset_key_y))

    # y become smaller
    dict_of_steps[Step.ONE.value] = sorted(dict_of_steps[Step.ONE.value], key=lambda x: abs(x[1]), reverse=True)
    # offset ratio become bigger
    dict_of_steps[Step.TWO.value] = sorted(dict_of_steps[Step.TWO.value], key=functools.cmp_to_key(compare))
    # x become bigger
    dict_of_steps[Step.THREE.value] = sorted(dict_of_steps[Step.THREE.value], key=lambda x: abs(x[0]))
    # offset ratio become smaller
    dict_of_steps[Step.FOUR.value] = sorted(dict_of_steps[Step.FOUR.value], key=functools.cmp_to_key(compare),
                                            reverse=True)
    # y become bigger
    dict_of_steps[Step.FIVE.value] = sorted(dict_of_steps[Step.FIVE.value], key=lambda x: abs(x[1]))
    # offset ratio become bigger
    dict_of_steps[Step.SIX.value] = sorted(dict_of_steps[Step.SIX.value], key=lambda x: abs(x[0] / x[1]))
    # x become smaller
    dict_of_steps[Step.SEVEN.value] = sorted(dict_of_steps[Step.SEVEN.value], key=lambda x: abs(x[0]), reverse=True)
    # offset ratio become smaller
    dict_of_steps[Step.EIGHT.value] = sorted(dict_of_steps[Step.EIGHT.value], key=lambda x: abs(x[0] / x[1]),
                                             reverse=True)
    return dict_of_steps


def find_the_best_asteroid():
    map_of_asteroids = get_list_of_input_tuple()
    max_count = len(get_dict_of_different_angles(map_of_asteroids[0]))
    best_asteroid = get_list_of_input_tuple()[0]
    for single_tuple in map_of_asteroids:
        current_count = len(get_dict_of_different_angles(single_tuple))
        if current_count > max_count:
            max_count = current_count
            best_asteroid = single_tuple
    print("best asteroid's max count=" + str(max_count))
    print("best asteroid=" + str(best_asteroid))
    return best_asteroid


def is_all_empty(key_offset_and_real_offset_dict, dict_of_steps):
    for key in dict_of_steps:
        tuple_key_list = dict_of_steps[key]
        for tuple_key in tuple_key_list:
            if len(key_offset_and_real_offset_dict[tuple_key]) > 0:
                return False
    return True


def get_solution_2():
    best_asteroid = find_the_best_asteroid()
    key_offset_and_real_offset_dict = get_dict_of_different_angles(best_asteroid)
    dict_of_steps = get_dict_of_steps(get_dict_of_different_angles(best_asteroid).keys())

    deletion_dict = {}
    i = 0
    while not is_all_empty(key_offset_and_real_offset_dict, dict_of_steps):
        for key in dict_of_steps:
            tuple_key_list = dict_of_steps[key]
            for tuple_key in tuple_key_list:
                if len(key_offset_and_real_offset_dict[tuple_key]) > 0:
                    i += 1
                    deletion_dict[i] = key_offset_and_real_offset_dict[tuple_key].pop(0)

    print(deletion_dict)
    print(deletion_dict[200])
    a, b = deletion_dict[200]
    return 100 * a + b


def compare(item1, item2):
    item1x, item1y = item1
    item2x, item2y = item2
    return item1x * item2y - item2x * item1y


if __name__ == "__main__":
    print(get_solution_2())

    list_of_tuple = [(1, 2), (3, 4), (7, 1), (1, 5), (6, 1), (3, 3)]
    # list_of_tuple_1 is better than list_of_tuple_2 is because it avoids comparing float. Float comparison is not reliable.
    list_of_tuple_1 = sorted(list_of_tuple, key=functools.cmp_to_key(compare))
    list_of_tuple_2 = sorted(list_of_tuple, key=lambda x: abs(x[0] / x[1]))
    print(list_of_tuple_1)
    print(list_of_tuple_2)
