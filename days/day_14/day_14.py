"""
Created at 2019-12-14 12:40

@author: jinyanliu
"""


def get_chemical_formula():
    chemical_formula_dict = {}
    with open("day_14_input_test_3") as lines:
        for line in lines:
            list_of_splitting = line.rstrip('\n').split(' => ')
            # print(list_of_splitting)
            list_for_dict = list_of_splitting[0].split(', ')
            # print(list_for_dict)

            chemical_formula_dict[list_of_splitting[1]] = list_for_dict
            # print(chemical_formula_dict)
            # print('\n')

    return chemical_formula_dict


def get_basic_element_count(chemical_formula_dict):
    list_for_item = chemical_formula_dict['1 FUEL']
    should_run = True

    while should_run:
        for item in list_for_item:
            number = item.split(' ')[0]
            chemical = item.split(' ')[1]
            if (not chemical == "NZVS") and (not chemical == "DCFZ") and (not chemical == "PSHF") and (
            not chemical == "HKGWZ") and (not chemical == "GPVTF"):
                for chemical_key in chemical_formula_dict.keys():
                    number_of_key = chemical_key.split(' ')[0]
                    chemical_name_of_key = chemical_key.split(' ')[1]
                    if chemical == chemical_name_of_key:
                        if int(number_of_key) >= int(number):
                            list_for_item.remove(item)
                            list_for_item += chemical_formula_dict[chemical_key]
                        else:
                            if int(number) % int(number_of_key) == 0:
                                times = int(number) / int(number_of_key)
                            else:
                                times = int(number) // int(number_of_key) + 1
                            list_for_item.remove(item)
                            list_for_item += (chemical_formula_dict[chemical_key] * int(times))

        has_only_ab = True
        for item in list_for_item:
            item_name = item.split(' ')[1]
            if (not item_name == "NZVS") and (not item_name == "DCFZ") and (not item_name == "PSHF") and (
            not item_name == "HKGWZ") and (not item_name == "GPVTF"):
                has_only_ab = False
                break

        if has_only_ab:
            should_run = False

    return list_for_item


def get_solution_1():
    basic_element_list = get_basic_element_count(get_chemical_formula())
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count_e = 0
    print(basic_element_list)
    for item in basic_element_list:
        item_count = item.split(' ')[0]
        item_name = item.split(' ')[1]
        if item_name == 'NZVS':
            count_a += int(item_count)
        elif item_name == 'DCFZ':
            count_b += int(item_count)
        elif item_name == 'PSHF':
            count_c += int(item_count)
        elif item_name == 'HKGWZ':
            count_d += int(item_count)
        elif item_name == 'GPVTF':
            count_e += int(item_count)
    if not count_a % 5 == 0:
        count_a = ((count_a // 5) + 1) * 5
    if not count_b % 6 == 0:
        count_b = ((count_b // 6) + 1) * 6
    if not count_c % 7 == 0:
        count_c = ((count_c // 7) + 1) * 7
    if not count_d % 5 == 0:
        count_d = ((count_d // 5) + 1) * 5
    if not count_e % 2 == 0:
        count_e = ((count_e // 2) + 1) * 2

    return count_a / 5 * 157 + count_b / 6 * 165 + count_c / 7 * 179 + count_d / 5 * 177 + count_e / 2 * 165


if __name__ == "__main__":
    print(get_chemical_formula())
    print(get_solution_1())
