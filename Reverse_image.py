from PIL import Image
import os
# Read an image file
path = os.path.dirname(os.path.abspath(__file__))
magic = path + '/' + 'natsuki.png'
image = Image.open(magic)
x, y = image.size
pim = image.load()
# Add some color boundaries to modify an image array
for height in range (x):
    for width in range (y):
        a=tuple((256-image.getpixel((height,width))[0],256-image.getpixel((height,width))[1],256-image.getpixel((height,width))[2]))
        pim[height,width]= a
# use pyplot to plot the image
image.show()