from PIL import Image

im = Image.open('monika.png') # Can be many different formats.
pix = im.load()
result=""
pixelload=0

i = 0
value = 0
bits = ''
text = ''
for k in range(330,470):
    for j in range(330,470):
        pixel = pix[k,j]
    mean = (pixel[0] + pixel[1] + pixel[2])/3
    bit = 1 if mean >= 128 else 0
    bits += str(bit)
    value = value | (bit << (7 - i))
    i += 1
    if i >= 8:
        text += chr(value)
        value = 0
        i = 0
    bits += '\n'
print (text)
print (im.size) # Get the width and hight of the image for iterating over
print (pix[0,0])  # Get the RGBA Value of the a pixel of an image
# pix[x,y] = value  # Set the RGBA Value of the image (tuple)
# im.save('alive_parrot.png')  # Save the modified pixels as .png