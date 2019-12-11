"""
Created at 2019-12-10 18:21

@author: jinyanliu
"""
import math


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


def get_tuple_sensor_count(base_tuple):
    list_of_different_angle = []
    basex, basey = base_tuple
    new_list = get_list_of_input_tuple()[:]
    new_list.remove(base_tuple)
    for tuple in new_list:
        currentx, currenty = tuple
        offsetx, offsety = basex - currentx, basey - currenty
        current_offset_gcd = math.gcd(offsetx, offsety)
        # Here we want to avoid using float. Float is unreliable at comparison.
        offsetx, offsety = offsetx // current_offset_gcd, offsety // current_offset_gcd
        current_tuple = (offsetx, offsety)
        if current_tuple not in list_of_different_angle:
            list_of_different_angle.append(current_tuple)
    return len(list_of_different_angle)


def get_solution_1():
    return max(list(map(get_tuple_sensor_count, get_list_of_input_tuple())))


if __name__ == "__main__":
    print(get_solution_1())
