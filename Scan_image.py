import cv2
import numpy as np
import os

path = os.path.dirname(os.path.abspath(__file__))
filename = path + 'Screen Shot 2020-05-30 at 23.32.34.png'
image = cv2.imread(filename)
cv2.imshow('Original', image)

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

adaptiveImage = cv2.adaptiveThreshold(grayImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('Scaned',adaptiveImage)
cv2.waitKey(0)

