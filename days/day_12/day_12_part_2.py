"""
Created at 2019-12-16 22:51

@author: jinyanliu
"""

from functools import reduce
from math import gcd


class Moon:
    def __init__(self, pos_x, pos_y, pos_z, vel_x, vel_y, vel_z):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.vel_z = vel_z

    def get_total_energy(self):
        return (abs(self.pos_x) + abs(self.pos_y) + abs(self.pos_z)) * (
                abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z))

    def __str__(self):
        return "Moon(" + str(self.pos_x) + ", " + str(self.pos_y) + ", " + str(self.pos_z) + ", " + str(
            self.vel_x) + ", " + str(self.vel_y) + ", " + str(self.vel_z) + ")"


def init_moons():
    # moon_1 = Moon(-1, 0, 2, 0, 0, 0)
    # moon_2 = Moon(2, -10, -7, 0, 0, 0)
    # moon_3 = Moon(4, -8, 8, 0, 0, 0)
    # moon_4 = Moon(3, 5, -1, 0, 0, 0)

    # moon_1 = Moon(-8, -10, 0, 0, 0, 0)
    # moon_2 = Moon(5, 5, 10, 0, 0, 0)
    # moon_3 = Moon(2, -7, 3, 0, 0, 0)
    # moon_4 = Moon(9, -8, -3, 0, 0, 0)

    moon_1 = Moon(4, 1, 1, 0, 0, 0)
    moon_2 = Moon(11, -18, -1, 0, 0, 0)
    moon_3 = Moon(-2, -10, -4, 0, 0, 0)
    moon_4 = Moon(-7, -2, 14, 0, 0, 0)
    return moon_1, moon_2, moon_3, moon_4


def lcm(*numbers):
    def lcm(a, b):
        return (a * b) // gcd(a, b)

    return reduce(lcm, numbers, 1)


def get_first_history_point(moon_1, moon_2, moon_3, moon_4):
    list_of_moons = [moon_1, moon_2, moon_3, moon_4]
    circle_x = circle_y = circle_z = 0
    i = 1

    while True:
        for outside_moon in list_of_moons:
            for inside_moon in list_of_moons:
                if not outside_moon == inside_moon:
                    if outside_moon.pos_x < inside_moon.pos_x:
                        outside_moon.vel_x += 1
                    elif outside_moon.pos_x > inside_moon.pos_x:
                        outside_moon.vel_x -= 1
                    if outside_moon.pos_y < inside_moon.pos_y:
                        outside_moon.vel_y += 1
                    elif outside_moon.pos_y > inside_moon.pos_y:
                        outside_moon.vel_y -= 1
                    if outside_moon.pos_z < inside_moon.pos_z:
                        outside_moon.vel_z += 1
                    elif outside_moon.pos_z > inside_moon.pos_z:
                        outside_moon.vel_z -= 1

        moon_1.pos_x += moon_1.vel_x
        moon_1.pos_y += moon_1.vel_y
        moon_1.pos_z += moon_1.vel_z
        moon_2.pos_x += moon_2.vel_x
        moon_2.pos_y += moon_2.vel_y
        moon_2.pos_z += moon_2.vel_z
        moon_3.pos_x += moon_3.vel_x
        moon_3.pos_y += moon_3.vel_y
        moon_3.pos_z += moon_3.vel_z
        moon_4.pos_x += moon_4.vel_x
        moon_4.pos_y += moon_4.vel_y
        moon_4.pos_z += moon_4.vel_z

        if moon_1.pos_x == 4 and moon_1.vel_x == 0 \
                and moon_2.pos_x == 11 and moon_2.vel_x == 0 \
                and moon_3.pos_x == -2 and moon_3.vel_x == 0 \
                and moon_4.pos_x == -7 and moon_4.vel_x == 0 and not bool(circle_x):
            circle_x = i

        if moon_1.pos_y == 1 and moon_1.vel_y == 0 \
                and moon_2.pos_y == -18 and moon_2.vel_y == 0 \
                and moon_3.pos_y == -10 and moon_3.vel_y == 0 \
                and moon_4.pos_y == -2 and moon_4.vel_y == 0 and not bool(circle_y):
            circle_y = i

        if moon_1.pos_z == 1 and moon_1.vel_z == 0 \
                and moon_2.pos_z == -1 and moon_2.vel_z == 0 \
                and moon_3.pos_z == -4 and moon_3.vel_z == 0 \
                and moon_4.pos_z == 14 and moon_4.vel_z == 0 and not bool(circle_z):
            circle_z = i

        if bool(circle_x) and bool(circle_y) and bool(circle_z):
            return lcm(circle_x, circle_y, circle_z)

        print(i)
        i += 1


def get_solution_2():
    moon_1, moon_2, moon_3, moon_4 = init_moons()
    return get_first_history_point(moon_1, moon_2, moon_3, moon_4)


if __name__ == "__main__":
    print(get_solution_2())
