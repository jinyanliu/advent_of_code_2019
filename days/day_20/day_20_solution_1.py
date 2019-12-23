"""
Created at 2019-12-23 19:14

@author: jinyanliu
"""


def get_dict_of_portals():
    dict_of_portals = {"HU": [(33, -2), (53, -86)],
                       "EU": [(43, -2), (33, -28)],
                       "AS": [(53, -2), (59, -86)],
                       "RN": [(59, -2), (28, -73)],
                       "ZV": [(69, -2), (84, -51)],
                       "KS": [(73, -2), (28, -45)],
                       "ZA": [(2, -31), (35, -86)],
                       "DY": [(2, -43), (84, -77)],
                       "KC": [(2, -45), (84, -61)],
                       "ZL": [(2, -47), (28, -57)],
                       "KL": [(2, -61), (84, -37)],
                       "AA": [(2, -63)],
                       "BI": [(2, -67), (57, -28)],
                       "KI": [(2, -73), (84, -45)],
                       "QO": [(2, -77), (28, -53)],
                       "PD": [(35, -112), (28, -39)],
                       "FO": [(41, -112), (53, -28)],
                       "XT": [(53, -112), (28, -33)],
                       "ZZ": [(59, -112)],
                       "OW": [(61, -112), (79, -86)],
                       "SW": [(67, -112), (75, -86)],
                       "GN": [(75, -112), (28, -77)],
                       "WV": [(79, -112), (45, -28)],
                       "LM": [(110, -37), (39, -86)],
                       "FA": [(110, -45), (75, -28)],
                       "ZU": [(110, -53), (67, -86)],
                       "QK": [(110, -59), (69, -28)],
                       "ND": [(110, -69), (28, -65)],
                       "XX": [(110, -73), (84, -69)]}
    return dict_of_portals


def get_input():
    with open("day_20_input") as lines:
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

    current_location_pathes = [[(2, -63)]]
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
