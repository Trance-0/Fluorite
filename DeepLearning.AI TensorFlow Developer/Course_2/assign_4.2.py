import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import keras
import tensorflow as tf

from tensorflow.keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Conv2D , MaxPool2D , Flatten , Dropout , BatchNormalization
from keras.preprocessing.image import ImageDataGenerator


def get_data(filename):
  # You will need to write code that will read the file passed
  # into this function. The first line contains the column headers
  # so you should ignore it
  # Each successive line contians 785 comma separated values between 0 and 255
  # The first value is the label
  # The rest are the pixel values for that picture
  # The function will return 2 np.array types. One with all the labels
  # One with all the images
  #
  # Tips:
  # If you read a full line (as 'row') then row[0] has the label
  # and row[1:785] has the 784 pixel values
  # Take a look at np.array_split to turn the 784 pixels into 28x28
  # You are reading in strings, but need the values to be floats
  # Check out np.array().astype for a conversion
    with open(filename) as training_file:
        images = np.empty((0, 28, 28), dtype=float)
        labels = np.empty((0), dtype=float)
        # Your code starts here
        raw_file = np.loadtxt(training_file.readlines()[
                              :-1], dtype=float, skiprows=1, delimiter=',')
        for row in progressbar(raw_file, "Loading data: "):
            if(len(row) == 785):
                labels = np.append(labels, row[0])
                image = np.reshape(row[1:785], (1, 28, 28))
                images = np.append(image, images, axis=0)
        print(f'read file:{filename} complete')
        return images, labels

