"""
Created at 2019-12-04 10:23

@author: jinyanliu
"""

start_number = 130254
end_number = 678275


def get_answer_to_question_1():
    valid_passwords = []
    for number in range(start_number, end_number):
        if is_sorted(number) and has_same_adjacent_digits(number):
            valid_passwords.append(number)
    return len(valid_passwords)


def is_sorted(number):
    sorted_number = int("".join(sorted(str(number))))
    if sorted_number == number:
        return True
    else:
        return False


def has_same_adjacent_digits(number):
    number_str = str(number)
    for i in range(0, 5):
        if number_str[i] == number_str[i + 1]:
            return True
    return False


if __name__ == "__main__":
    print("Answer to question 1 = ", get_answer_to_question_1())
    print("Answer to question 2 = ")
