"""
Created at 2019-12-14 20:42

@author: jinyanliu
"""

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import random


fig = pyplot.figure()
ax = Axes3D(fig)

sequence_containing_x_vals = [4,11,-2,-7]
sequence_containing_y_vals = [1,-18,-10,-2]
sequence_containing_z_vals = [1,-1,-4,14]

random.shuffle(sequence_containing_x_vals)
random.shuffle(sequence_containing_y_vals)
random.shuffle(sequence_containing_z_vals)

ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals)
pyplot.show()



set_1 = set()
set_1.add(2)
set_1.clear()
print(set_1)
