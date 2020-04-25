from PIL import Image
import os
# Read an image file


def wavelength_to_rgb(wavelength, gamma=0.8):
    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    R *= 255
    G *= 255
    B *= 255
    return (int(R), int(G), int(B))
 
def chaotic(a):
    alen=len(a)
    xlim=10
    ylim=10
    while alen>100:
        alen=alen/100
        xlim=xlim*10
        ylim=ylim*10
    image = Image.new("RGB",(xlim,ylim),(255,255,255)) 
    x, y = image.size
    pim = image.load()
    time=0
# Add some color boundaries to modify an image array
    tot=list(a)
    for height in range (x):
        for width in range (y):
            time+=1
            if(time<len(tot)):
                r=int(ord(tot[height*width+width].encode('utf-8').decode('utf-8')))//256**2
                g=int(ord(tot[height*width+width].encode('utf-8').decode('utf-8')))//256%256
                b=int(ord(tot[height*width+width].encode('utf-8').decode('utf-8')))%256
                a=tuple((r,g,b))
                pim[height,width]= a
# use pyplot to plot the image
    image.show()

print('Input the text that you need to encode.')
a=input()
print(chaotic(a))
