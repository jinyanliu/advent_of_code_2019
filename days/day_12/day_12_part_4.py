"""
Created at 2019-12-15 00:19

@author: jinyanliu
"""


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


def adjust_moons(moon_1, moon_2, moon_3, moon_4):
    should_stop = False
    i = 0

    dict_of_moon_1_pos_x = []
    dict_of_moon_1_pos_y = []
    dict_of_moon_1_pos_z = []
    dict_of_moon_1_vel_x = []
    dict_of_moon_1_vel_y = []
    dict_of_moon_1_vel_z = []

    dict_of_moon_2_pos_x = []
    dict_of_moon_2_pos_y = []
    dict_of_moon_2_pos_z = []
    dict_of_moon_2_vel_x = []
    dict_of_moon_2_vel_y = []
    dict_of_moon_2_vel_z = []

    dict_of_moon_3_pos_x = []
    dict_of_moon_3_pos_y = []
    dict_of_moon_3_pos_z = []
    dict_of_moon_3_vel_x = []
    dict_of_moon_3_vel_y = []
    dict_of_moon_3_vel_z = []

    dict_of_moon_4_pos_x = []
    dict_of_moon_4_pos_y = []
    dict_of_moon_4_pos_z = []
    dict_of_moon_4_vel_x = []
    dict_of_moon_4_vel_y = []
    dict_of_moon_4_vel_z = []

    list_of_moons = [moon_1, moon_2, moon_3, moon_4]

    while not should_stop:
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

        if moon_1.pos_x == 4:
            dict_of_moon_1_pos_x.append(i)
        if moon_1.pos_y == 1:
            dict_of_moon_1_pos_y.append(i)
        if moon_1.pos_z == 1:
            dict_of_moon_1_pos_z.append(i)
        if moon_1.vel_x == 0:
            dict_of_moon_1_vel_x.append(i)
        if moon_1.vel_y == 0:
            dict_of_moon_1_vel_y.append(i)
        if moon_1.vel_z == 0:
            dict_of_moon_1_vel_z.append(i)

        if moon_2.pos_x == 11:
            dict_of_moon_2_pos_x.append(i)
        if moon_2.pos_y == -18:
            dict_of_moon_2_pos_y.append(i)
        if moon_2.pos_z == -1:
            dict_of_moon_2_pos_z.append(i)
        if moon_2.vel_x == 0:
            dict_of_moon_2_vel_x.append(i)
        if moon_2.vel_y == 0:
            dict_of_moon_2_vel_y.append(i)
        if moon_2.vel_z == 0:
            dict_of_moon_2_vel_z.append(i)

        if moon_3.pos_x == -2:
            dict_of_moon_3_pos_x.append(i)
        if moon_3.pos_y == -10:
            dict_of_moon_3_pos_y.append(i)
        if moon_3.pos_z == -4:
            dict_of_moon_3_pos_z.append(i)
        if moon_3.vel_x == 0:
            dict_of_moon_3_vel_x.append(i)
        if moon_3.vel_y == 0:
            dict_of_moon_3_vel_y.append(i)
        if moon_3.vel_z == 0:
            dict_of_moon_3_vel_z.append(i)

        if moon_4.pos_x == -7:
            dict_of_moon_4_pos_x.append(i)
        if moon_4.pos_y == -2:
            dict_of_moon_4_pos_y.append(i)
        if moon_4.pos_z == 14:
            dict_of_moon_4_pos_z.append(i)
        if moon_4.vel_x == 0:
            dict_of_moon_4_vel_x.append(i)
        if moon_4.vel_y == 0:
            dict_of_moon_4_vel_y.append(i)
        if moon_4.vel_z == 0:
            dict_of_moon_4_vel_z.append(i)




        if (bool(dict_of_moon_1_pos_x) and bool(dict_of_moon_1_pos_y) and bool(dict_of_moon_1_pos_z)
                and bool(dict_of_moon_1_vel_x) and bool(dict_of_moon_1_vel_y) and bool(dict_of_moon_1_vel_z)
                and bool(dict_of_moon_2_pos_x) and bool(dict_of_moon_2_pos_y) and bool(dict_of_moon_2_pos_z)
                and bool(dict_of_moon_2_vel_x) and bool(dict_of_moon_2_vel_y) and bool(dict_of_moon_2_vel_z)
                and bool(dict_of_moon_3_pos_x) and bool(dict_of_moon_3_pos_y) and bool(dict_of_moon_3_pos_z)
                and bool(dict_of_moon_3_vel_x) and bool(dict_of_moon_3_vel_y) and bool(dict_of_moon_3_vel_z)
                and bool(dict_of_moon_4_pos_x) and bool(dict_of_moon_4_pos_y) and bool(dict_of_moon_4_pos_z)
                and bool(dict_of_moon_4_vel_x) and bool(dict_of_moon_4_vel_y) and bool(dict_of_moon_4_vel_z)):
            print(dict_of_moon_1_pos_x)
            print(dict_of_moon_1_pos_y)
            print(dict_of_moon_1_pos_z)
            print(dict_of_moon_1_vel_x)
            print(dict_of_moon_1_vel_y)
            print(dict_of_moon_1_vel_z)

            print(dict_of_moon_2_pos_x)
            print(dict_of_moon_2_pos_y)
            print(dict_of_moon_2_pos_z)
            print(dict_of_moon_2_vel_x)
            print(dict_of_moon_2_vel_y)
            print(dict_of_moon_2_vel_z)

            print(dict_of_moon_3_pos_x)
            print(dict_of_moon_3_pos_y)
            print(dict_of_moon_3_pos_z)
            print(dict_of_moon_3_vel_x)
            print(dict_of_moon_3_vel_y)
            print(dict_of_moon_3_vel_z)

            print(dict_of_moon_4_pos_x)
            print(dict_of_moon_4_pos_y)
            print(dict_of_moon_4_pos_z)
            print(dict_of_moon_4_vel_x)
            print( dict_of_moon_4_vel_y)
            print(dict_of_moon_4_vel_z)
            print("i=" + str(i))
            should_stop = True



        print("i=" + str(i))
        i += 1


def get_solution_1():
    moon_1, moon_2, moon_3, moon_4 = init_moons()
    adjust_moons(moon_1, moon_2, moon_3, moon_4)
    # return moon_1.get_total_energy() + moon_2.get_total_energy() + moon_3.get_total_energy() + moon_4.get_total_energy()


if __name__ == "__main__":
    print(get_solution_1())
