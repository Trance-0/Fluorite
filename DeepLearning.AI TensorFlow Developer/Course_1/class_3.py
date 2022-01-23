import tensorflow as tf
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
from tensorflow.keras import models

# callback function to cancel traing when reaching specific accuracy.
class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch,logs={}):
        if(logs.get('loss')<0.4):
            print("\Loss is low so canelling training!")
            self.model.stop_training = True

def visualize():
    print(test_labels[:100])

    f, axarr = plt.subplots(3,4)

    FIRST_IMAGE=0
    SECOND_IMAGE=23
    THIRD_IMAGE=28
    CONVOLUTION_NUMBER = 1

    layer_outputs = [layer.output for layer in model.layers]
    activation_model = tf.keras.models.Model(inputs = model.input, outputs = layer_outputs)

    for x in range(0,4):
        f1 = activation_model.predict(test_images[FIRST_IMAGE].reshape(1, 28, 28, 1))[x]
        axarr[0,x].imshow(f1[0, : , :, CONVOLUTION_NUMBER], cmap='inferno')
        axarr[0,x].grid(False)
  
        f2 = activation_model.predict(test_images[SECOND_IMAGE].reshape(1, 28, 28, 1))[x]
        axarr[1,x].imshow(f2[0, : , :, CONVOLUTION_NUMBER], cmap='inferno')
        axarr[1,x].grid(False)
  
        f3 = activation_model.predict(test_images[THIRD_IMAGE].reshape(1, 28, 28, 1))[x]
        axarr[2,x].imshow(f3[0, : , :, CONVOLUTION_NUMBER], cmap='inferno')
        axarr[2,x].grid(False)

# call your stupid callback class
callbacks = myCallback()

fashion_mnist=keras.datasets.fashion_mnist
(training_images,training_labels),(test_images,test_labels)=fashion_mnist.load_data()

# Normalize the pixel values of the train and test images, they work better with smaller values.
training_images  = training_images / 255.0
test_images = test_images / 255.0

# Reshape the dataset to meet Conv2D requirement
training_shape=(len(training_images),training_images[0].shape[0],training_images[0].shape[1],1)
training_images=training_images.reshape(training_shape)
test_shape=(len(test_images),test_images[0].shape[0],test_images[0].shape[1],1)
test_images=test_images.reshape(test_shape)

model = keras.Sequential([
    keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)),
    keras.layers.MaxPooling2D(2,2),
    keras.layers.Conv2D(32,(3,3),activation='relu'),
#   Where 64 means you add 64 filters with (3,3) size, 28,28,1 28 is the image size and 1 byte for color depth 

    keras.layers.MaxPooling2D(2,2),
#   means you will get the greatest value in the 2 by 2 pixel value.

    keras.layers.Flatten(),
    keras.layers.Dense(128,activation='relu'),
#   The hidden layer

    keras.layers.Dense(10,activation='softmax')
])

# to inspect the sexy model
model.summary()

model.compile(optimizer = tf.optimizers.Adam(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
print(f'\nMODEL TRAINING:')
model.fit(training_images, training_labels, epochs=5,callbacks=[callbacks])

# Evaluate on the test set
print(f'\nMODEL EVALUATION:')
test_loss = model.evaluate(test_images, test_labels)

# visualize()

