# import the necessary packages
from skimage.measure import compare_ssim
import argparse
import imutils
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#denoise the image by the kernelSize
def denoise(img,kernelSize):
    kernel = np.ones((kernelSize,kernelSize), np.uint8)
    img=cv.dilate(img, kernel, iterations = 1)
    kernel = np.ones((kernelSize,kernelSize), np.uint8)
    img=cv.erode(img, kernel, iterations = 1)
    return img


def lineImage(img,kernelSize):
    
    #edge_image = extract_edge(gray_image)
    edge_image = cv.Canny(img, 100, kernelSize, L2gradient = True)
    return edge_image

# def lineImage(img,kernelSize):
    
#     gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     #edge_image = extract_edge(gray_image)
#     edge_image = cv.Canny(gray_image, 100, kernelSize, L2gradient = True)
#     return edge_image

#start to capture image from camera, 0 is the default value of the system
cap = cv.VideoCapture(0)
#if the camera is opened
if not cap.isOpened():
    print("Cannot open camera")
    exit()

#some global variables
lineScale=150
noiseScale=3
threshold=70
init=True
imageA= None

#infinite loop
while True:
    #capture frame, ret is the image recieve status, and frame is the data
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    #set the first picture
    if init:
        imageA= frame
        init=False
        continue
    else:
        imageB = frame
    #convert the images to grayscale
    
    tempA = denoise(cv.cvtColor(imageA, cv.COLOR_BGR2GRAY),noiseScale)
    tempB = denoise(cv.cvtColor(imageB, cv.COLOR_BGR2GRAY),noiseScale)
    # grayA = lineImage(tempA,lineScale)
    # grayB = lineImage(tempB,lineScale)
    # grayA = denoise(tempA,noiseScale)
    # grayB = denoise(tempB,noiseScale)
    #get the difference value between the two image, returns a value between 1~0
    #score is the differece 
    #diff is the image which likes[[0,1,1],[0,0,0],[1,0,0]]
    (score, diff) = compare_ssim(tempA, tempB, full=True)
    #convert the 2d array diff to a uint8 picture
    diff = (diff * 255).astype("uint8")
    # threshold the difference image, followed by finding contours to
    # obtain the regions of the two input images that differ
    thresh = cv.threshold(diff, 0, 255,
    cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]
    cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL,
    cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # loop over the contours
    output=imageB.copy()
    for c in cnts:
    # compute the bounding box of the contour and then draw the
    # bounding box on both input images to represent where the two
    # images differ
        (x, y, w, h) = cv.boundingRect(c)
        if w>threshold and h>threshold:
            cv.rectangle(output, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # Display the resulting frame
    imageA=imageB
    
    cv.imshow('frame',output)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

# construct the argument parse and parse the arguments
# load the two input images

# show the output images
