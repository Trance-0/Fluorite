## This is course material for Introduction to Python Scientific Programming
## Class 17 Example code: 3D_linear_system_plot.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

x, y = np.meshgrid(range(-5, 5), range(-5, 5))

z1 = 3*x + 2*y -1
z2 = (1/4)*(-2 - 2*x + 2*y)
z3 = -x + 0.5*y

ax3d = plt.axes(projection = '3d')
ax3d.plot_surface(x, y, z1, color = 'red', alpha = 0.5 )
ax3d.plot_surface(x, y, z2, color = 'green', alpha = 0.5 )
ax3d.plot_surface(x, y, z3, color = 'blue', alpha = 0.5 )

ax3d.scatter(1, -2, -2, 'ko')
plt.show()