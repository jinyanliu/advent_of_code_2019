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


def get_one_phase(target_string):
    len_of_string = len(target_string)
    print(target_string)
    one_phase_result = ""
    for i in range(0, len_of_string):
        multiple_int_list = get_multiply_int_list(i + 1, len_of_string)
        one_line_result = 0
        string_to_print = ""
        for i in range(0, len_of_string):
            a = int(target_string[i])
            b = multiple_int_list[i]
            one_line_result += a * b
            string_to_print += str(a) + ' * '+ str(b) + ' + '
        one_line_result_str = str(one_line_result)[-1]
        string_to_print = string_to_print[:-3]  + ' = '+ str(one_line_result)[-1]
        print(string_to_print)
        one_phase_result += one_line_result_str

    return one_phase_result


def get_solution_one(initial_string, phase_number):
    target_string = initial_string
    for p in range(0,phase_number):
        print(p)
        target_string = get_one_phase(target_string)
        print('\n')
    return target_string


def get_solution_two(initial_string, phase_number):
    target_string = initial_string
    for p in range(0, phase_number):
        print(p)
        target_string = get_one_phase(target_string)
    position = target_string[:7]
    return target_string[int(position):]


if __name__ == "__main__":
    print(get_solution_one(get_original_string(), 100))
    #print(get_solution_two(get_original_string()*10000, 100))

