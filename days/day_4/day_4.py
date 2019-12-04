"""
Created at 2019-12-04 10:23

@author: jinyanliu
"""
from days.day_4.constant import START_NUMBER, END_NUMBER, DIGITS_LIMIT


def get_valid_password_list_to_question_1():
    valid_passwords = []
    for number in range(START_NUMBER, END_NUMBER):
        if is_sorted(number) and has_multiple_same_adjacent_digits(number):
            valid_passwords.append(number)
    return valid_passwords


def get_answer_to_question_1():
    return len(get_valid_password_list_to_question_1())


def get_answer_to_question_2():
    valid_passwords = []
    for number in range(START_NUMBER, END_NUMBER):
        if is_sorted(number) and has_2_same_adjacent_digits(number):
            valid_passwords.append(number)
    return len(valid_passwords)


def is_sorted(number):
    sorted_number = int("".join(sorted(str(number))))
    return True if sorted_number == number else False


def has_multiple_same_adjacent_digits(number):
    number_str = str(number)
    for i in range(0, DIGITS_LIMIT - 1):
        if number_str[i] == number_str[i + 1]:
            return True
    return False


def has_2_same_adjacent_digits(number):
    number_str = str(number)

    if number_str[0] == number_str[1] and number_str[1] != number_str[2]:
        return True
    if number_str[DIGITS_LIMIT - 2] == number_str[DIGITS_LIMIT - 1] \
            and number_str[DIGITS_LIMIT - 2] != number_str[DIGITS_LIMIT - 3]:
        return True
    for i in range(1, DIGITS_LIMIT - 1):
        if number_str[i] == number_str[i + 1] and number_str[i] != number_str[i - 1] and number_str[i + 1] != \
                number_str[i + 2]:
            return True
    return False


def get_solution_2():
    return len(list(filter(is_matching_extra_condition_in_solution_2, get_valid_password_list_to_question_1())))


def is_matching_extra_condition_in_solution_2(num):
    c_to_count = {}

    for c in str(num):
        if c in c_to_count:
            c_to_count[c] += 1
        else:
            c_to_count[c] = 1

    return 2 in c_to_count.values()


if __name__ == "__main__":
    print("Answer to question 1 = ", get_answer_to_question_1())
    print("Answer to question 2 = ", get_answer_to_question_2())
    print("Solution 2 = ", get_solution_2())
