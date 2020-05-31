import cv2
import numpy as np
import os

# load file
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/64711378_p0_master1200.jpg'
image = cv2.imread(filename)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('Edge_Image')

intensity=200
def on_change(val):
    global intensity
    intensity=cv2.getTrackbarPos('intensity','Edge_Image')

cv2.createTrackbar('intensity','Edge_Image',0,1000,on_change)
cv2.setTrackbarPos('intensity','Edge_Image', 200)
#返回滑块所在位置对应的值

while 1:
    #edge_image = extract_edge(gray_image)
    edge_image = cv2.Canny(gray_image, 100,intensity, L2gradient = True)

    cv2.imshow('Edge Image', edge_image)
    cv2.waitKey(1)
    if cv2.waitKey(1)==ord("q"):
        break
cv2.destroyAllWindows()