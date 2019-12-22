"""
Created at 2019-12-22 18:30

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


def move_right(current_location, map, list_of_visited):
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


def move_left(current_location, map, list_of_visited):
    current_x, current_y = current_location
    up_location = (current_x, current_y + 1)
    down_location = (current_x, current_y - 1)
    left_location = (current_x - 1, current_y)
    right_location = (current_x + 1, current_y)

    if up_location not in list_of_visited and map[up_location] == ".":
        current_location = up_location
    elif left_location not in list_of_visited and map[left_location] == ".":
        current_location = left_location
    elif down_location not in list_of_visited and map[down_location] == ".":
        current_location = down_location
    elif right_location not in list_of_visited and map[right_location] == ".":
        current_location = right_location


    elif up_location in map.keys() and map[up_location] == ".":
        current_location = up_location
    elif left_location in map.keys() and map[left_location] == ".":
        current_location = left_location
    elif down_location in map.keys() and map[down_location] == ".":
        current_location = down_location
    elif right_location in map.keys() and map[right_location] == ".":
        current_location = right_location

    if should_mark_as_wall(current_location, map):
        map[current_location] = "#"
    print(current_location)
    # plot_message(map)
    return current_location


def reach_character(current_location, map):
    character = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    up, down, left, right = get_4_locations(current_location)

    if map[current_location] == "." \
            and ((map.get(up, "0") in character)
                 or (map.get(right, "0") in character)
                 or (map.get(down, "0") in character)
                 or (map.get(left, "0") in character)):
        print("Found character!" + str(current_location))
        return True
    return False


def get_right_destination_and_steps(start_location):
    map = get_input()
    # plot_message(map)

    current_location = start_location
    reach_portal = False
    list_of_visited = []
    count_of_steps = 0
    while not reach_portal:
        list_of_visited.append(current_location)
        current_location = move_right(current_location, map, list_of_visited)
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
        current_location = move_right(current_location, map, list_of_visited)
        count_of_steps += 1
        reach_portal = reach_character(current_location, map)
        # plot_message(map)
    print(count_of_steps)
    return count_of_steps


def get_left_destination_and_steps(start_location):
    map = get_input()
    plot_message(map)

    current_location = start_location
    reach_portal = False
    list_of_visited = []
    count_of_steps = 0
    while not reach_portal:
        list_of_visited.append(current_location)
        current_location = move_left(current_location, map, list_of_visited)
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
        current_location = move_left(current_location, map, list_of_visited)
        count_of_steps += 1
        reach_portal = reach_character(current_location, map)
        # plot_message(map)
    print(count_of_steps)
    return count_of_steps


def get_4_locations(center):
    x, y = center
    up = (x, y + 1)
    down = (x, y - 1)
    left = (x - 1, y)
    right = (x + 1, y)
    return up, down, left, right


def move(map, current_pathes):
    pathes = []
    for path in current_pathes:
        location = path[-1]
        up, down, left, right = get_4_locations(location)
        possible_location_list = []
        if map.get(up, "0") == ".":
            possible_location_list.append(up)
        if map.get(down, "0") == ".":
            possible_location_list.append(down)
        if map.get(left, "0") == ".":
            possible_location_list.append(left)
        if map.get(right, "0") == ".":
            possible_location_list.append(right)
        for possible_location in possible_location_list:
            if possible_location not in path:
                new_path = path + [possible_location]
                if reach_character(possible_location, map):
                    print(len(new_path) - 1)
                pathes.append(new_path)
                print(new_path)
    return pathes


def process(map, location):
    initial_pathes = [[location]]
    current_pathes = initial_pathes
    last_pathes = []
    while current_pathes != last_pathes:
        last_pathes = current_pathes
        current_pathes = move(map, last_pathes)


if __name__ == "__main__":
    map = get_input()

    aa = (19, -2)
    process(map, aa)
    ###############################
    # Found: AS(17,-8), CP(21,-8) #
    ###############################

    asas = (32, -17)
    process(map, asas)
    #####################
    # Found: QG(26,-17) #
    #####################

    cp = (19, -34)
    process(map, cp)
    #####################
    # Found: JP(21,-28) #
    #####################
