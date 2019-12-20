"""
Created at 2019-12-19 22:51

@author: jinyanliu
"""


def get_original_string():
    with open("day_16_input_test_2") as lines:
        original_string = lines.readline()
    return original_string * 10000


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


def get_phase_target_string(phase, start_index, end_index):
    print(phase)
    target_string = get_original_string()
    if phase == 1:
        # print("Phase " + str(phase) + " result string = " + target_string)
        return target_string[start_index:end_index]
    else:
        result_string = ""
        last_phase_target_string = get_phase_target_string(phase - 1, 0, len(target_string))
        for i in range(1, len(target_string) + 1):
            result_string += get_one_row_result(last_phase_target_string, i)
        # print("Phase " + str(phase) + " result string = " + result_string)
        return result_string


def get_solution_1():
    return get_phase_target_string(101, 0, 7)


if __name__ == "__main__":
    print(get_solution_1())
    print(len(get_original_string()))
