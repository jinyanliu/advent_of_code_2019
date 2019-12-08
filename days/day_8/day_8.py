"""
Created at 2019-12-08 10:42

@author: jinyanliu
"""


def get_original_string():
    with open("day_8_input") as lines:
        original_string = lines.readline()
    return original_string


def split_list(original_list, total_digits_of_one_layer):
    return [original_list[i:i + total_digits_of_one_layer] for i in
            range(0, len(original_list), total_digits_of_one_layer)]


def get_solution_1():
    string_lists = split_list(get_original_string(), 25 * 6)
    dict_of_counts_0 = {}
    for i in range(0, len(string_lists)):
        dict_of_counts_0[i] = 0
        for s in string_lists[i]:
            if s == '0':
                dict_of_counts_0[i] += 1

    min_counts_of_0 = dict_of_counts_0[0]
    min_counts_of_0_index = 0
    j = 0
    for j in dict_of_counts_0.keys():
        if dict_of_counts_0[j] < min_counts_of_0:
            min_counts_of_0 = dict_of_counts_0[j]
            min_counts_of_0_index = j

    target_string = string_lists[min_counts_of_0_index]
    count_of_1 = 0
    count_of_2 = 0
    for a in target_string:
        if a == '1':
            count_of_1 += 1
        elif a == '2':
            count_of_2 += 1
    return count_of_2 * count_of_1


if __name__ == "__main__":
    print(get_solution_1())
