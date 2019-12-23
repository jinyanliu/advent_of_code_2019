"""
Created at 2019-12-22 18:30

@author: jinyanliu
"""
import matplotlib.pyplot


def get_dict_of_portals():
    dict_of_portals = {"ZZ": [(2, -17)],
                       "DI": [(2, -15), (8, -21)],
                       "YN": [(2, -23), (26, -13)],
                       "VT": [(32, -11), (26, -23)],
                       "LF": [(32, -21), (15, -28)],
                       "JP": [(15, -34), (21, -28)],
                       "CP": [(19, -34), (21, -8)],
                       "AA": [(19, -2)],
                       "QG": [(32, -23), (26, -17)],
                       "AS": [(32, -17), (17, -8)],
                       "BU": [(26, -21), (11, -34)],
                       "JO": [(13, -28), (2, -19)]}
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


def process(map, location):
    current_pathes = [[location]]
    current_steps = [[0]]
    last_pathes = []
    last_steps = []
    while current_pathes != last_pathes:
        last_pathes = current_pathes
        last_steps = current_steps
        current_pathes, current_steps = move(map, last_pathes, last_steps)
    return current_pathes, current_steps


def move(map, current_pathes, current_steps):
    pathes = []
    steps = []
    i = 0
    for path in current_pathes:
        has_possible_locations = False
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
                has_possible_locations = True
                new_path = path + [possible_location]
                new_step = current_steps[i] + [(len(new_path) - 1)]
                if reach_character(possible_location, map):
                    print(len(new_path) - 1)
                pathes.append(new_path)
                steps.append(new_step)
                # print(new_path)
        if not has_possible_locations:
            pathes.append(path)
            steps.append(current_steps[i])
        i += 1
    return pathes, steps


def continue_find_next_portal(map, portals_dict, current_location_pathes, current_name_pathes, current_step_pathes):
    location_pathes = []
    name_pathes = []
    steps_pathes = []
    i = 0
    for path in current_location_pathes:
        has_new_portal = False
        portal_location = path[-1]
        target_location = portal_location
        portal = ""
        for key, value in portals_dict.items():
            if portal_location in value:
                portal = key
        if len(portals_dict[portal]) == 1:
            target_location = portals_dict[portal][0]
        else:
            for location in portals_dict[portal]:
                if not location == portal_location:
                    target_location = location
        processed_pathes, processed_steps = process(map, target_location)

        for key, value in portals_dict.items():
            for location in value:
                j = 0
                for processed_path in processed_pathes:
                    if processed_path[-1] == location and location not in path and key not in current_name_pathes[i]:
                        has_new_portal = True
                        new_location_path = path + [location]
                        new_name_path = current_name_pathes[i] + [key]
                        result_steps = processed_steps[j]
                        new_step_path = current_step_pathes[i] + [result_steps]
                        print(new_location_path)
                        print(new_name_path)
                        print(new_step_path)
                        location_pathes.append(new_location_path)
                        name_pathes.append(new_name_path)
                        steps_pathes.append(new_step_path)
                    j += 1

        if not has_new_portal:
            location_pathes.append(path)
            name_pathes.append(current_name_pathes[i])
            steps_pathes.append(current_step_pathes[i])
        i += 1
    return location_pathes, name_pathes, steps_pathes


if __name__ == "__main__":
    map = get_input()
    portals_dict = get_dict_of_portals()

    current_location_pathes = [[(19, -2)]]
    current_name_pathes = [["AA"]]
    current_steps_pathes = [[0]]
    last_location_pathes = []
    last_name_pathes = []
    last_step_pathes = []
    while current_location_pathes != last_location_pathes:
        last_location_pathes = current_location_pathes
        last_name_pathes = current_name_pathes
        last_step_pathes = current_steps_pathes
        current_location_pathes, current_name_pathes, current_steps_pathes = continue_find_next_portal(map,
                                                                                                       portals_dict,
                                                                                                       last_location_pathes,
                                                                                                       last_name_pathes,
                                                                                                       last_step_pathes)

    result_pathes = []
    result_steps = []
    i = 0
    for current_name_path in current_name_pathes:
        if "ZZ" in current_name_path:
            result_pathes.append(current_name_path)
            print(current_name_path)
            result_steps.append(current_steps_pathes[i])
            print(current_steps_pathes[i])
        i += 1

    k = 0
    while k < len(result_pathes):
        current_path = result_pathes[k]
        current_step_path = result_steps[k]
        print(current_step_path)

        l = 0
        step = 0
        should_stop = False
        while l < len(current_path) and not should_stop:
            current_portal = current_path[l]
            current_step = current_step_path[l]

            if (l == 0):
                step += 0
            else:
                step += current_step[-1]
            l += 1

            if (current_portal == "ZZ"):
                should_stop = True
        print("step:" + str(step + l - 2))

        k += 1
