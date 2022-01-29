import numpy as np
import csv
import matplotlib.pyplot as plt
import keras
import tensorflow as tf

from tensorflow.keras.utils import to_categorical
from keras.preprocessing.image import ImageDataGenerator
from os import getcwd

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
        # Your code starts here
        raw_file = np.loadtxt(training_file.readlines()[
                              :-1], dtype=float, skiprows=1, delimiter=',')
        labels=np.array([i[0] for i in raw_file])
        images=np.array([i[1:785] for i in raw_file])
        images=images.reshape(-1,28,28)
        print(f'read file:{filename} complete')
        return images, labels


# full data set
path_sign_mnist_train = f'{getcwd()}/tmp2/sign_mnist_train.csv'
path_sign_mnist_test = f'{getcwd()}/tmp2/sign_mnist_test.csv'

# reduce training set
# path_sign_mnist_train = f'{getcwd()}/tmp2/sign_mnist_train_a.csv'
# path_sign_mnist_test = f'{getcwd()}/tmp2/sign_mnist_test_a.csv'

training_images, training_labels = get_data(path_sign_mnist_train)
testing_images, testing_labels = get_data(path_sign_mnist_test)

training_labels = to_categorical(training_labels, 25)
testing_labels = to_categorical(testing_labels,25)

training_images = training_images / 255.0
testing_images = testing_images / 255.0

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

fig = plt.figure(figsize = (8, 8))
rows, columns = 4, 4

for i in range(1, (rows * columns) + 1):
    imageIndex = i
    fig.add_subplot(rows, columns, i)
    plt.imshow(training_images[imageIndex], cmap = 'gray')
    
plt.show()

# In this section you will have to add another dimension to the data
# So, for example, if your array is (10000, 28, 28)
# You will need to make it (10000, 28, 28, 1)
# Hint: np.expand_dims

dataGenerator = tf.keras.preprocessing.image.ImageDataGenerator(
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
        rescale = 1 / 255.0)  # Normalization output


training_images = np.reshape(training_images, (-1, 28, 28, 1))
testing_images = np.reshape(testing_images, (-1, 28, 28, 1))
                                
dataGenerator.fit(training_images)
# Keep These
print(training_images.shape)
print(testing_images.shape)

# Their output should be:
# (27455, 28, 28, 1)
# (7172, 28, 28, 1)

model = tf.keras.models.Sequential([
    # Your Code Here
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu',
                           input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(25, activation='softmax')
])

model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate = 0.0005) , loss = 'categorical_crossentropy' , metrics = ['accuracy'])

model.summary()

history = model.fit(dataGenerator.flow(training_images, training_labels, batch_size = 16) ,epochs = 10, 
                    validation_data = (testing_images, testing_labels))

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
