"""
Created at 2019-12-20 19:43

@author: jinyanliu
"""
import matplotlib.pyplot


def get_dict_of_portals():
    dict_of_portals = {"zz": (2, -17),
                       "di": (2, -15)}
    return dict_of_portals


def get_input():
    with open("day_20_input_test_1") as lines:
        dict_of_map = {}
        y = 0
        for line in lines:
            x = 0
            for s in line:
                dict_of_map[x, y] = s
                x += 1
            y -= 1
        print(dict_of_map)
        return dict_of_map


def plot_message(dict_of_map):
    list_of_wall = []
    list_of_route = []

    for key, value in dict_of_map.items():
        if value == "#":
            list_of_wall.append(key)
        if value == ".":
            list_of_route.append(key)

    if len(list_of_route) > 0:
        g, h = zip(*list_of_route)
        matplotlib.pyplot.scatter(g, h, c='pink', marker="4", s=20)

    if len(list_of_wall) > 0:
        i, j = zip(*list_of_wall)
        matplotlib.pyplot.scatter(i, j, c='black', marker="s", s=20)

    matplotlib.pyplot.show()


def should_mark_as_wall(current_location, map):
    currentx, currenty = current_location
    if ((currentx, currenty + 1) in map.keys() and map[
        (currentx, currenty + 1)] == "#"
            and (currentx + 1, currenty) in map.keys() and map[
                (currentx + 1, currenty)] == "#"
            and (currentx, currenty - 1) in map.keys() and map[
                (currentx, currenty - 1)] == "#"):
        return True

    if ((currentx - 1, currenty) in map.keys() and map[
        (currentx - 1, currenty)] == "#"
            and (currentx + 1, currenty) in map.keys() and map[
                (currentx + 1, currenty)] == "#"
            and (currentx, currenty - 1) in map.keys() and map[
                (currentx, currenty - 1)] == "#"):
        return True

    if ((currentx - 1, currenty) in map.keys() and map[
        (currentx - 1, currenty)] == "#"
            and (currentx, currenty + 1) in map.keys() and map[
                (currentx, currenty + 1)] == "#"
            and (currentx, currenty - 1) in map.keys() and map[
                (currentx, currenty - 1)] == "#"):
        return True

    if ((currentx - 1, currenty) in map.keys() and map[
        (currentx - 1, currenty)] == "#"
            and (currentx, currenty + 1) in map.keys() and map[
                (currentx, currenty + 1)] == "#"
            and (currentx + 1, currenty) in map.keys() and map[
                (currentx + 1, currenty)] == "#"):
        return True

    return False


def move(current_location, map, list_of_visited):
    current_x, current_y = current_location
    up_location = (current_x, current_y + 1)
    down_location = (current_x, current_y - 1)
    left_location = (current_x - 1, current_y)
    right_location = (current_x + 1, current_y)

    if up_location not in list_of_visited and map[up_location] == ".":
        current_location = up_location
    elif right_location not in list_of_visited and map[right_location] == ".":
        current_location = right_location
    elif down_location not in list_of_visited and map[down_location] == ".":
        current_location = down_location
    elif left_location not in list_of_visited and map[left_location] == ".":
        current_location = left_location
    elif up_location in map.keys() and map[up_location] == ".":
        current_location = up_location
    elif right_location in map.keys() and map[right_location] == ".":
        current_location = right_location
    elif down_location in map.keys() and map[down_location] == ".":
        current_location = down_location
    elif left_location in map.keys() and map[left_location] == ".":
        current_location = left_location

    if should_mark_as_wall(current_location, map):
        map[current_location] = "#"
    print(current_location)
    # plot_message(map)
    return current_location


def reach_character(current_location, map):
    character = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    current_x, current_y = current_location
    up_location = (current_x, current_y + 1)
    down_location = (current_x, current_y - 1)
    left_location = (current_x - 1, current_y)
    right_location = (current_x + 1, current_y)

    if map[current_location] == "." and ((up_location in map.keys() and map[up_location] in character)
                                         or (right_location in map.keys() and map[right_location] in character)
                                         or (down_location in map.keys() and map[down_location] in character)
                                         or (left_location in map.keys() and map[left_location] in character)):
        print("Found character!" + str(current_x) + "," + str(current_y))
        return True
    return False


def get_destination_and_steps(start_location):
    map = get_input()
    # plot_message(map)

    current_location = start_location
    reach_portal = False
    list_of_visited = []
    count_of_steps = 0
    while not reach_portal:
        list_of_visited.append(current_location)
        current_location = move(current_location, map, list_of_visited)
        count_of_steps += 1
        reach_portal = reach_character(current_location, map)
        # plot_message(map)
    print(count_of_steps)

    current_location = start_location
    reach_portal = False
    list_of_visited = []
    count_of_steps = 0
    while not reach_portal:
        list_of_visited.append(current_location)
        current_location = move(current_location, map, list_of_visited)
        count_of_steps += 1
        reach_portal = reach_character(current_location, map)
        # plot_message(map)
    print(count_of_steps)
    return count_of_steps


if __name__ == "__main__":
    zz = (2, -17)
    steps1 = get_destination_and_steps(zz)
    di = (2, -15)
    di = (8, -21)
    steps2 = get_destination_and_steps(di)
    yn = (2, -23)
    yn = (26, -13)
    steps3 = get_destination_and_steps(yn)
    vt = (32, -11)
    vt = (26, -23)
    steps4 = get_destination_and_steps(vt)
    lf = (32, -21)
    lf = (15, -28)
    steps5 = get_destination_and_steps(lf)
    jp = (15, -34)
    jp = (21, -28)
    steps6 = get_destination_and_steps(jp)
    cp = (19, -34)
    cp = (21, -8)
    steps7 = get_destination_and_steps(cp)
    aa = (19, -2)

    steps = steps1+steps2+steps3+steps4+steps5+steps6+steps7
    print(steps)
