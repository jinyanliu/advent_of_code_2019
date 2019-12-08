"""
Created at 2019-12-08 11:26

@author: jinyanliu
"""


def get_original_string():
    with open("day_8_input") as lines:
        original_string = lines.readline()
    return original_string


def split_list(list_to_split, len_of_each_split_chunk):
    return [list_to_split[i:i + len_of_each_split_chunk] for i in range(0, len(list_to_split), len_of_each_split_chunk)]


def convert_string_to_dict(string):
    dict_of_index_and_char = {}
    for i in range(0, len(string)):
        dict_of_index_and_char[i] = string[i]
    return dict_of_index_and_char


def get_solution_2(wide_pixel, tall_pixel):
    string_lists = split_list(get_original_string(), wide_pixel * tall_pixel)
    list_of_dict = list(map(convert_string_to_dict, string_lists))

    final_dict = {}
    for i in range(0, wide_pixel * tall_pixel):
        for j in range(0, len(list_of_dict)):
            if list_of_dict[j][i] == '0':
                final_dict[i] = '1'
                break
            if list_of_dict[j][i] == '1':
                final_dict[i] = ' '
                break

    final_string = ''
    for value in final_dict.values():
        final_string += str(value)

    for line in split_list(final_string, 25):
        print(line)


if __name__ == "__main__":
    get_solution_2(25, 6)
