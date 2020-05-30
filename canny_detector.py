## This is course material for Introduction to Modern Artificial Intelligence
## Class 5 Example code: canny_detector.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import cv2
import numpy as np
import os

# load file
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/highway_video.mp4'
outputFilename = path + '/output_video.avi'

grabber = cv2.VideoCapture(filename)
fps = int(grabber.get(cv2.CAP_PROP_FPS))
width = int(grabber.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(grabber.get(cv2.CAP_PROP_FRAME_HEIGHT))
output = cv2.VideoWriter(outputFilename, cv2.VideoWriter_fourcc('M', 'J', 'P','G'),\
     fps, (width, height), False)

def region_of_interest(image, height= None, width = None):
    if image is None:
        if (height is None) or (width is None):
            return None
    else:
        height,width = image.shape

    ROI = np.array([(0, height-100), (width, height-100), (width, height-300), (0, height-300)])
    mask = np.zeros([height, width], dtype = np.uint8)
    cv2.fillPoly(mask, [ROI], 255)
    return mask

mask_image = region_of_interest(None, height, width)

while(grabber.isOpened()):
    ret, frame = grabber.read()

    if ret == False:
        break

    # Create gray image and denoise
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #edge_image = extract_edge(gray_image)
    edge_image = cv2.Canny(gray_image, 100, 200, L2gradient = True)
    ROI_image = cv2.bitwise_and(edge_image,mask_image)

    cv2.imshow('Edge Image', ROI_image)
    output.write(ROI_image)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

grabber.release()
output.release()
cv2.destroyAllWindows()
