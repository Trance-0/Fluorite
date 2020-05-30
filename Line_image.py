import cv2
import numpy as np
import os

# load file
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/64711378_p0_master1200.jpg'
image = cv2.imread(filename)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#edge_image = extract_edge(gray_image)
edge_image = cv2.Canny(gray_image, 100, 200, L2gradient = True)

cv2.imshow('Edge Image', edge_image)
cv2.waitKey(0)