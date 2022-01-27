# ATTENTION: Please do not alter any of the provided code in the exercise. Only add your own code where indicated
# ATTENTION: Please do not add or remove any cells in the exercise. The grader will check specific cells based on the cell position.
# ATTENTION: Please use the provided epoch values when training.

import matplotlib.pyplot as plt
import csv
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from os import getcwd
import sys


def progressbar(it, prefix="", size=29, file=sys.stdout):
    # This def is made by: https://stackoverflow.com/users/1207193/iambr
    # it is the list you are going to iterate
    # prefix is the title of your progress bar
    # size is the length of your progress bar
    count = len(it)

    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s%s] %i/%i\r" %
                   (prefix, "="*x, ">", "."*(size-x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()


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


# full data set
# path_sign_mnist_train = f'{getcwd()}/tmp2/sign_mnist_train.csv'
# path_sign_mnist_test = f'{getcwd()}/tmp2/sign_mnist_test.csv'

# reduce training set
path_sign_mnist_train = f'{getcwd()}/tmp2/sign_mnist_train_a.csv'
path_sign_mnist_test = f'{getcwd()}/tmp2/sign_mnist_test_a.csv'

training_images, training_labels = get_data(path_sign_mnist_train)
testing_images, testing_labels = get_data(path_sign_mnist_test)

training_images=training_images/255.
testing_images=testing_images/255.

# Keep these
print(training_images.shape)
print(training_labels.shape)
print(testing_images.shape)
print(testing_labels.shape)
print(testing_labels)

# Their output should be:
# (27455, 28, 28)
# (27455,)
# (7172, 28, 28)
# (7172,)

# Testing code, do not submit them to your assignment!
plt.imshow(testing_images[1], interpolation='nearest')
plt.show()
print(testing_labels[1])

# In this section you will have to add another dimension to the data
# So, for example, if your array is (10000, 28, 28)
# You will need to make it (10000, 28, 28, 1)
# Hint: np.expand_dims

train_datagen = ImageDataGenerator(
   featurewise_center=False,  # set input mean to 0 over the dataset
        samplewise_center=False,  # set each sample mean to 0
        featurewise_std_normalization=False,  # divide inputs by std of the dataset
        samplewise_std_normalization=False,  # divide each input by its std
        zca_whitening=False,  # apply ZCA whitening
        rotation_range=14,  # randomly rotate images in the range (degrees, 0 to 180)
        zoom_range = 0.09, # Randomly zoom image 
        width_shift_range=0.14,  # randomly shift images horizontally (fraction of total width)
        height_shift_range=0.14,  # randomly shift images vertically (fraction of total height)
        horizontal_flip=False,  # randomly flip images
        vertical_flip=False,   # randomly flip images
        brightness_range = (0.8, 1.0),  # brightness of image
        rescale = 1. / 255.)

validation_datagen = ImageDataGenerator(rescale=1./255.)

training_images = np.reshape(training_images, (-1,28,28,1))
train_datagen.fit(training_images)
testing_images = np.reshape(testing_images,(-1,28,28,1))

training_labels=tf.keras.utils.to_categorical(training_labels,num_classes=25)
testing_labels=tf.keras.utils.to_categorical(testing_labels, num_classes=25)

batch_size = 16

train_generator = train_datagen.flow(
    training_images,
    training_labels, batch_size=batch_size)

validation_generator = validation_datagen.flow(
    testing_images,
    testing_labels, batch_size=batch_size)
# Keep These
print(training_images.shape)
print(testing_images.shape)

# Their output should be:
# (27455, 28, 28, 1)
# (7172, 28, 28, 1)

# Define the model
# Use no more than 2 Conv2D and 2 MaxPooling2D
model = tf.keras.models.Sequential([
    # Your Code Here
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu',
                           input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(25, activation='softmax')
])

# Compile Model.
model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.005),loss='categorical_crossentropy',metrics=['accuracy'])

model.summary()

# Train the Model
history = model.fit_generator(train_generator,
                              validation_data=validation_generator,
                              steps_per_epoch=len(training_images)//batch_size,
                              epochs=10,
                              validation_steps=len(testing_images)//batch_size
                              )

# model.evaluate(testing_images/255., testing_labels, verbose=0)

# Plot the chart for accuracy and loss on both training and validation
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'r', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.legend()
plt.figure()

plt.plot(epochs, loss, 'r', label='Training Loss')
plt.plot(epochs, val_loss, 'b', label='Validation Loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()
