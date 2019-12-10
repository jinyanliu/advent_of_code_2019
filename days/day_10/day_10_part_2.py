"""
Created at 2019-12-10 20:29

@author: jinyanliu
"""

"""
Created at 2019-12-10 18:21

@author: jinyanliu
"""
import math


def get_list_of_input_tuple():
    list_of_input_tuple = []
    with open("day_10_test_input_6") as lines:
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
        print(offsetx, offsety)
        current_offset_gcd = math.gcd(offsetx, offsety)
        offsetx, offsety = offsetx / current_offset_gcd, offsety / current_offset_gcd
        current_tuple = (offsetx, offsety)
        if current_tuple not in list_of_different_angle:
            list_of_different_angle.append(current_tuple)
    return len(list_of_different_angle)


def find_the_sensor():
    map_of_asteroids = get_list_of_input_tuple()
    max_count = get_tuple_sensor_count(map_of_asteroids[0])
    best_asteroid = get_list_of_input_tuple()[0]
    for single_tuple in map_of_asteroids:
        current_count = get_tuple_sensor_count(single_tuple)
        if current_count > max_count:
            max_count = current_count
            best_asteroid = single_tuple
    print(max_count)
    print(best_asteroid)


def get_solution_1():
    return max(list(map(get_tuple_sensor_count, get_list_of_input_tuple())))


if __name__ == "__main__":
    #print(get_solution_1())
    #find_the_sensor()

    get_tuple_sensor_count((8,3))
