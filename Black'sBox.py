
## This is course material for Introduction to Python Scientific Programming

## Class 18 Example code: multiple_minima.py

## Author: Allen Y. Yang,  Intelligent Racing Inc.

##

## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use



import numpy as np

import matplotlib.pyplot as plt

from matplotlib.widgets import Cursor



fig = plt.figure()

ax = plt.axes()

ax.set_xlim([-5, 5])

ax.set_ylim([-5, 5])

ax.spines['left'].set_position(('data', 0))

ax.spines['bottom'].set_position(('data', 0))

ax.spines['right'].set_color('none')

ax.spines['top'].set_color('none')



# Function y = 1/4 x^4 + 1/3 x^3 - x^2 - 2 

def func(x):

    return 1/4*x**4 + 1/3*x**3 - x**2 - 2



def grad(x):

    return x**3 + x**2 - 2*x



x = np.arange(-5, 5, 0.1)

y = func(x)



plt.plot(x, y, 'r-', linewidth = 3)

line = None

def onclick(event):

    global line



    if not line == None:

        line.remove()



    epsilon = [0.05,0.02,0.01,0.005,0.001]

    learn_rate =[5,2,1,0.5,0.1]

    delta = np.inf

    xlist = [event.xdata]

    ylist = [func(event.xdata)]

    repeat_time = 0

    for n in range(5):

            while delta > epsilon[-n-1]:

                x_next = xlist[-1] - learn_rate[-n-1]*grad(xlist[-1])

                delta = abs(xlist[-1] - x_next)

                xlist.append(x_next)

                ylist.append(func(x_next))

        

        for n in range(5):

            while delta > epsilon[-n-1]:

                x_next = xlist[-1] + learn_rate[-n-1]*grad(xlist[-1])

                delta = abs(xlist[-1] - x_next)

                xlist.append(x_next)

                ylist.append(func(x_next))

                repeat_time += 1

        

        for a in range(repeat_time-1):

            del.xlist[-2-a]

            del.ylist[-2-a]



        repeat_time = 0



    while xlist[-1] != -5 and xlist[-1] != 5:

        for n in range(5):

            while delta > epsilon[-n-1]:

                x_next = xlist[-1] - learn_rate[-n-1]*grad(xlist[-1])

                delta = abs(xlist[-1] - x_next)

                xlist.append(x_next)

                ylist.append(func(x_next))

        

        for n in range(5):

            while delta > epsilon[-n-1]:

                x_next = xlist[-1] + learn_rate[-n-1]*grad(xlist[-1])

                delta = abs(xlist[-1] - x_next)

                xlist.append(x_next)

                ylist.append(func(x_next))

                repeat_time += 1

        

        for a in range(repeat_time-1):

            del.xlist[-2-a]

            del.ylist[-2-a]



        repeat_time = 0





    line, = plt.plot(xlist, ylist, 'bo-')



cursor = Cursor(ax, horizOn = True, vertOn = True, color = 'green')

fig.canvas.mpl_connect('button_press_event',onclick)



plt.show()