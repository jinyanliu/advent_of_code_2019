"""
Created at 2019-12-12 14:35

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


# moon_1 = Moon(-1, 0, 2, 0, 0, 0)
# moon_2 = Moon(2, -10, -7, 0, 0, 0)
# moon_3 = Moon(4, -8, 8, 0, 0, 0)
# moon_4 = Moon(3, 5, -1, 0, 0, 0)

#moon_1 = Moon(-8, -10, 0, 0, 0, 0)
#moon_2 = Moon(5, 5, 10, 0, 0, 0)
#moon_3 = Moon(2, -7, 3, 0, 0, 0)
#moon_4 = Moon(9, -8, -3, 0, 0, 0)

moon_1 = Moon(4, 1, 1, 0, 0, 0)
moon_2 = Moon(11, -18, -1, 0, 0, 0)
moon_3 = Moon(-2, -10, -4, 0, 0, 0)
moon_4 = Moon(-7, -2, 14, 0, 0, 0)
print(moon_1)
print(moon_2)
print(moon_3)
print(moon_4)
print("\n")



for i in range(0, 1000):

    list_of_moons = [moon_1, moon_2, moon_3, moon_4]

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

    print(moon_1)
    print(moon_2)
    print(moon_3)
    print(moon_4)
    print("\n")

print(moon_1.get_total_energy() + moon_2.get_total_energy() + moon_3.get_total_energy() + moon_4.get_total_energy())
