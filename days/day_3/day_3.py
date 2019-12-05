"""
Created at 2019-12-03 10:10

@author: jinyanliu
"""


def get_2_lists_of_input():
    with open('day_3_input') as inputs:
        input_1 = inputs.readline().split(',')
        input_2 = inputs.readline().split(',')
    return [input_1, input_2]


def get_answer_to_question_1():
    list_1 = get_2_lists_of_input()[0]
    list_2 = get_2_lists_of_input()[1]
    list_of_intersection_tuples = get_intersection_tuple_list(get_list_of_route(list_1), get_list_of_route(list_2))
    return get_distance_of_closest_intersection(list_of_intersection_tuples)


def get_distance_of_closest_intersection(list_of_intersection_tuples):
    a, b = list_of_intersection_tuples[0]
    current_result = abs(a) + abs(b)
    for tu in list_of_intersection_tuples:
        c, d = tu
        if abs(c) + abs(d) < current_result:
            current_result = abs(c) + abs(d)
    return current_result


def get_answer_to_question_2():
    list_1 = get_2_lists_of_input()[0]
    list_2 = get_2_lists_of_input()[1]
    list_of_intersection_tuples = get_intersection_tuple_list(get_list_of_route(list_1), get_list_of_route(list_2))
    return get_min_total_steps(list_1, list_2, list_of_intersection_tuples)


def get_min_total_steps(list_1, list_2, list_intersections):
    dict_1 = get_intersection_steps_dict(list_1, list_intersections)
    dict_2 = get_intersection_steps_dict(list_2, list_intersections)

    final_dict = {}
    for ke in dict_1.keys():
        final_dict[ke] = dict_1[ke] + dict_2[ke]
    return min(final_dict.values())


def get_list_of_route(list_of_instructions):
    list_of_tuple = []
    for ins in list_of_instructions:
        last_tuple_item = (0, 0) if (len(list_of_tuple) == 0) else list_of_tuple[-1]
        last_x, last_y = last_tuple_item

        direction = ins[0]
        step = int(ins[1:])
        if direction == "R":
            for time in range(0, step):
                list_of_tuple.append((last_x + time + 1, last_y))

        if direction == "L":
            for time in range(0, step):
                list_of_tuple.append((last_x - time - 1, last_y))

        if direction == "U":
            for time in range(0, step):
                list_of_tuple.append((last_x, last_y + time + 1))

        if direction == "D":
            for time in range(0, step):
                list_of_tuple.append((last_x, last_y - time - 1))

    return list_of_tuple


def get_intersection_tuple_list(first_route_tuple_list, second_route_tuple_list):
    return list(set(first_route_tuple_list) & set(second_route_tuple_list))


def get_intersection_steps_dict(list_of_instructions, list_of_cross_points):
    list_of_tuple = []
    total_steps = 0
    dict_of_steps = {}
    for ins in list_of_instructions:

        last_tuple_item = (0, 0) if (len(list_of_tuple) == 0) else list_of_tuple[-1]
        last_x, last_y = last_tuple_item

        direction = ins[0]
        step = int(ins[1:])
        if direction == "R":
            for time in range(0, step):
                total_steps += 1
                current_x_y = (last_x + time + 1, last_y)
                list_of_tuple.append(current_x_y)
                if (current_x_y in list_of_cross_points) and (current_x_y not in dict_of_steps.keys()):
                    dict_of_steps[current_x_y] = total_steps

        if direction == "L":
            for time in range(0, step):
                total_steps += 1
                current_x_y = (last_x - time - 1, last_y)
                list_of_tuple.append(current_x_y)
                if (current_x_y in list_of_cross_points) and (current_x_y not in dict_of_steps.keys()):
                    dict_of_steps[current_x_y] = total_steps

        if direction == "U":
            for time in range(0, step):
                total_steps += 1
                current_x_y = (last_x, last_y + time + 1)
                list_of_tuple.append(current_x_y)
                if (current_x_y in list_of_cross_points) and (current_x_y not in dict_of_steps.keys()):
                    dict_of_steps[current_x_y] = total_steps

        if direction == "D":
            for time in range(0, step):
                total_steps += 1
                current_x_y = (last_x, last_y - time - 1)
                list_of_tuple.append(current_x_y)
                if (current_x_y in list_of_cross_points) and (current_x_y not in dict_of_steps.keys()):
                    dict_of_steps[current_x_y] = total_steps

    return dict_of_steps


if __name__ == "__main__":
    print("Answer to question 1 = ", get_answer_to_question_1())
    print("Answer to question 2 = ", get_answer_to_question_2())
