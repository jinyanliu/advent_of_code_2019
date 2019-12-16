"""
Created at 2019-12-16 16:36

@author: jinyanliu
"""
import numpy as np

0, 1, 0, -1
12345678


def get_original_string():
    with open("day_16_input_test_1") as lines:
        original_string = lines.readline()
    return original_string


def get_multiply_int_list(row, target_len):
    new_list = []
    list_1 = [0, 1, 0, -1]
    list_2 = list(np.repeat(list_1, row))
    if len(list_2) >= target_len + 1:
        new_list = list_2
    else:
        repeat_times = target_len // len(list_2)
        reminder = target_len % len(list_2)
        for i in range(0, repeat_times + 1):
            new_list += list_2
        new_list += list_2[:reminder]
    return new_list[1:target_len + 1]


def get_solution_1(target_string):
    len_of_string = len(target_string)
    one_phase_result = ""
    for i in range(0, len_of_string):
        multiple_int_list = get_multiply_int_list(i + 1, len_of_string)
        one_line_result = 0
        for i in range(0, len_of_string):
            a = int(target_string[i])
            b = multiple_int_list[i]
            one_line_result += a * b
        one_line_result_str = str(one_line_result)[-1]
        one_phase_result += one_line_result_str
    return one_phase_result


if __name__ == "__main__":
    print(get_multiply_int_list(4, 8))

    print(get_solution_1(get_original_string()))
