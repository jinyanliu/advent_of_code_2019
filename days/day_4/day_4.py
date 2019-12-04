"""
Created at 2019-12-04 10:23

@author: jinyanliu
"""

start_number = 130254
end_number = 678275


def get_answer_to_question_1():
    valid_passwords = []
    for number in range(start_number, end_number):
        if (is_sorted(number)):
            valid_passwords.append(number)
    return valid_passwords


def is_sorted(number):
    sorted_number = int("".join(sorted(str(number))))
    if sorted_number == number:
        return True
    else:
        return False


if __name__ == "__main__":
    print("Answer to question 1 = ", get_answer_to_question_1())
    print("Answer to question 2 = ")
    print(is_sorted(1234566666666789))
