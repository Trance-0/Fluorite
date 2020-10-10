import cv2
import numpy as np
import os
import tkinter as tk

h=200
w=300
root = tk.Tk()
T = tk.Text(root, height=h, width=w)
T.pack()


# load file
scale=[" ",".",",",":",";","_","-","^","\\","/",">","=","P","W","M","#","@"]
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/IMG_3494.JPG'
temp=""

image = cv2.imread(filename)
image = cv2.resize(image, (w, h))
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image.shape)
width= image.shape[0]
height=image.shape[1]
for i in range (width):
    for j in range(height):
        print((gray_image[i,j])//16)
        temp+= (scale[(gray_image[i,j])//16])
    temp+="\n"

T.insert(tk.END, temp)
tk.mainloop()
cv2.imshow("gray",gray_image)
k=cv2.waitKey(0)
if k == ord('q'): # wait for 's' key to save and exit
    cv2.destroyAllWindows()