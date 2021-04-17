from matplotlib import image
from matplotlib import pyplot
import numpy as np
import os
def list_avarage(l):
    tot=0
    for i in range (len(l)):
        tot+=l[i]
    return tot/len(l)

# Read an image file
path = os.path.dirname(os.path.abspath(__file__))
magic = path + '/' + 'Screen Shot 2020-04-23 at 22.19.34.png'
data = image.imread(magic)
print (data)