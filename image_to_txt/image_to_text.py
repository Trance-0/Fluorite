import cv2
import numpy as np
import os
import tkinter as tk

#picture size
h=100
w=200

window = tk.Tk()
window.title('My Window')
window.geometry("1600x800") 
var=tk.StringVar()
l = tk.Label(window, textvariable=var,bg='white', fg='black', font=('TkDefaultFont', 8), width=w*5)

# load file
scale=[" ",".",",",":",";","_","-","^","\\","/",">","=","P","W","M","#","@"]
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/002.JPG'
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
        temp+= (scale[(256-gray_image[i,j])//16])
    temp+="\n"

var.set(temp)
l.pack()
tk.mainloop()

# cv2.imshow("gray",gray_image)
# k=cv2.waitKey(0)
# if k == ord('q'): 
#     cv2.destroyAllWindows()