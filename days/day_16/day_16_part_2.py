"""
Created at 2019-12-17 14:30

@author: jinyanliu
"""
import numpy as np


def get_original_string():
    with open("day_16_input") as lines:
        original_string = lines.readline()
    return original_string


# def get_multiply_int_list(row, target_len):
#     new_list = []
#     list_1 = [0, 1, 0, -1]
#     list_2 = list(np.repeat(list_1, row))
#     if len(list_2) >= target_len + 1:
#         new_list = list_2
#     else:
#         repeat_times = target_len // len(list_2)
#         reminder = target_len % len(list_2)
#         for i in range(0, repeat_times + 1):
#             new_list += list_2
#         new_list += list_2[:reminder]
#     return new_list[1:target_len + 1]


# def get_one_phase(target_string):
#     len_of_string = len(target_string)
#     one_phase_result = ""
#     for i in range(1, len_of_string + 1):
#         one_phase_result += get_one_row_result(target_string, i)
#     print(one_phase_result)
#     return one_phase_result


def get_one_row_result(target_string, row_number):
    result = 0
    i = 0
    length = len(target_string)
    while i < length:
        for j in range(0, row_number):
            current_index_one = i + row_number - 1 + j
            if current_index_one < length:
                result += int(target_string[current_index_one])
        for k in range(0, row_number):
            current_index_minus_one = i + 3 * row_number - 1 + k
            if current_index_minus_one < length:
                result -= int(target_string[current_index_minus_one])
        i += 4 * row_number
    # print("One row int result="+str(result))
    # print("One row string single result="+ str(result)[-1])
    return str(result)[-1]


def get_phase_target_string(phase):
    print(phase)
    target_string = get_original_string()
    if phase == 1:
        #print("Phase " + str(phase) + " result string = " + target_string)
        return target_string
    else:
        result_string = ""
        last_phase_target_string = get_phase_target_string(phase - 1)
        for i in range(1, len(target_string) + 1):
            result_string += get_one_row_result(last_phase_target_string, i)
        #print("Phase " + str(phase) + " result string = " + result_string)
        return result_string


def get_solution_1():
    return get_phase_target_string(101)


if __name__ == "__main__":
    print(get_solution_1())
    print(len(get_original_string()))
