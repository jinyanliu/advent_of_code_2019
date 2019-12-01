"""
Created at 2019-12-01 10:45

@author: jinyanliu
"""


def get_list_of_int_input():
    list_of_int = []
    with open("day_1_input") as lines:
        for line in lines:
            list_of_int.append(int(line.rstrip('\n')))
    return list_of_int


def get_base_fuel(weight):
    return (weight // 3) - 2


def get_total_fuel_for_one_mass(mass):
    current_fuel = get_base_fuel(mass)
    total_fuel = current_fuel
    string_result = str(total_fuel)
    while current_fuel > 0:
        current_fuel = get_base_fuel(current_fuel)
        if current_fuel > 0:
            total_fuel += current_fuel
            string_result += " + " + str(current_fuel)
    string_result += " = " + str(total_fuel)
    print(string_result)
    return total_fuel


def get_total_fuel_for_masses(list_of_masses):
    result = 0
    string_result = str(result)

    for i in list_of_masses:
        result += get_total_fuel_for_one_mass(i)
        string_result += str(get_total_fuel_for_one_mass(i)) + " + "

    new_string_result = string_result[1:-3]
    final_string_result = new_string_result + " = " + str(result)
    print(final_string_result)
    return result


if __name__ == "__main__":
    get_total_fuel_for_masses(get_list_of_int_input())
