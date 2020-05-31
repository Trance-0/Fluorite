import cv2
import numpy as np
import os

path = os.path.dirname(os.path.abspath(__file__))
filename = path + 'Screen Shot 2020-05-30 at 23.32.34.png'
image = cv2.imread(filename)
cv2.imshow('Original', image)
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#新建一个滑动条
cv2.createTrackbar('intensity','Original',0,255,None)
#返回滑块所在位置对应的值
intensity=cv2.getTrackbarPos('intensity','img')
adaptiveImage = cv2.adaptiveThreshold(grayImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, intensity, 1)
cv2.imshow('Scaned',adaptiveImage)
cv2.waitKey(0)
