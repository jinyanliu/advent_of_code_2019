"""
Created at 2019-12-14 12:40

@author: jinyanliu
"""


def get_chemical_formula():
    chemical_formula_dict = {}
    with open("day_14_input") as lines:
        for line in lines:
            list_of_splitting = line.rstrip('\n').split(' => ')
            list_for_dict = list_of_splitting[0].split(', ')
            chemical_formula_dict[list_of_splitting[1]] = list_for_dict
    return chemical_formula_dict


def get_basic_element_count(chemical_formula_dict):
    list_for_item = chemical_formula_dict['1 FUEL']
    should_run = True
    dict_of_leftover_item ={}
    for item in chemical_formula_dict.keys():
        chemical = item.split(' ')[1]
        dict_of_leftover_item[chemical] = 0

    while should_run:
        for item in list_for_item:
            number = item.split(' ')[0]
            chemical = item.split(' ')[1]

            if chemical == "ORE":
                continue

            left_over = dict_of_leftover_item[chemical]
            if int(number) == left_over:
                dict_of_leftover_item[chemical] = 0
                list_for_item.remove(item)
                number = 0
            elif int(number) > left_over:
                dict_of_leftover_item[chemical] = 0
                list_for_item.remove(item)
                new_item = chemical + ' '+str(int(number)-left_over)
                list_for_item.append(new_item)
                number = int(number)-left_over
            elif int(number)<left_over:
                dict_of_leftover_item[chemical] = left_over - int(number)
                list_for_item.remove(item)
                number = 0

            if not number == 0:
                for chemical_key in chemical_formula_dict.keys():
                    number_of_key = chemical_key.split(' ')[0]
                    chemical_name_of_key = chemical_key.split(' ')[1]
                    if chemical == chemical_name_of_key:
                        if int(number_of_key) >= int(number):
                            dict_of_leftover_item[chemical] += int(number_of_key)-int(number)
                            list_for_item.remove(new_item)
                            list_for_item += chemical_formula_dict[chemical_key]
                        else:
                            if int(number) % int(number_of_key) == 0:
                                times = int(number) / int(number_of_key)
                            else:
                                times = int(number) // int(number_of_key) + 1
                                leftover_item_count = (int(number) // int(number_of_key) + 1) * int(number_of_key) - int(number)
                                dict_of_leftover_item[chemical] += leftover_item_count
                            list_for_item.remove(new_item)
                            list_for_item += (chemical_formula_dict[chemical_key] * int(times))
                        break

        has_only_ab = True
        for item in list_for_item:
            item_name = item.split(' ')[1]
            if not item_name == "ORE":
                has_only_ab = False
                break

        if has_only_ab:
            should_run = False

    return list_for_item


def get_solution_1(dict):
    basic_element_list = get_basic_element_count(dict)
    final_count = 0
    for item in basic_element_list:
        final_count += int(item.split(' ')[0])

    print(basic_element_list)
    print(final_count)


if __name__ == "__main__":
    get_solution_1(get_chemical_formula())



