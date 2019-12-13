"""
Created at 2019-12-12 23:25

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
    #moon_1 = Moon(-1, 0, 2, 0, 0, 0)
    #moon_2 = Moon(2, -10, -7, 0, 0, 0)
    #moon_3 = Moon(4, -8, 8, 0, 0, 0)
    #moon_4 = Moon(3, 5, -1, 0, 0, 0)

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

    dict_of_moon_1_history = {}
    dict_of_moon_2_history = {}
    dict_of_moon_3_history = {}
    dict_of_moon_4_history = {}

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

        moon_1_list = [moon_1.pos_x, moon_1.pos_y, moon_1.pos_z, moon_1.vel_x, moon_1.vel_y, moon_1.vel_z]
        moon_2_list = [moon_2.pos_x, moon_2.pos_y, moon_2.pos_z, moon_2.vel_x, moon_2.vel_y, moon_2.vel_z]
        moon_3_list = [moon_3.pos_x, moon_3.pos_y, moon_3.pos_z, moon_3.vel_x, moon_3.vel_y, moon_3.vel_z]
        moon_4_list = [moon_4.pos_x, moon_4.pos_y, moon_4.pos_z, moon_4.vel_x, moon_4.vel_y, moon_4.vel_z]

        for key in dict_of_moon_1_history.keys():
            if dict_of_moon_1_history[key] == moon_1_list \
                    and dict_of_moon_2_history[key] == moon_2_list \
                    and dict_of_moon_3_history[key] == moon_3_list \
                    and dict_of_moon_4_history[key] == moon_4_list:
                print("i=" + str(i))
                print("key=" + str(key))
                should_stop = True

        dict_of_moon_1_history[i] = moon_1_list
        dict_of_moon_2_history[i] = moon_2_list
        dict_of_moon_3_history[i] = moon_3_list
        dict_of_moon_4_history[i] = moon_4_list

        if i % 10000 == 0:
            print("i=" + str(i))

        i += 1


def get_solution_1():
    moon_1, moon_2, moon_3, moon_4 = init_moons()
    adjust_moons(moon_1, moon_2, moon_3, moon_4)
    # return moon_1.get_total_energy() + moon_2.get_total_energy() + moon_3.get_total_energy() + moon_4.get_total_energy()


if __name__ == "__main__":
    print(get_solution_1())
