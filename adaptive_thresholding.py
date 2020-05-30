## This is course material for Introduction to Modern Artificial Intelligence
## Class 5 Example code: adaptive_thresholding.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import cv2
import numpy as np
import os

path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/bookpage.jpg'
image = cv2.imread(filename)
cv2.imshow('Original', image)

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Process 1: Using simple thresholding
_, threshImage = cv2.threshold(grayImage, 20, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold', threshImage)

# Process 2: Using adaptive thresholding
adaptiveImage = cv2.adaptiveThreshold(grayImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('Adaptive',adaptiveImage)
cv2.waitKey(0)