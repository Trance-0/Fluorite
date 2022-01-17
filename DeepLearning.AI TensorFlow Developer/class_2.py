import tensorflow as tf
import numpy as np
from tensorflow import keras

# callback function to cancel traing when reaching specific accuracy.
class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch,logs={}):
        if(logs.get('loss')<0.4):
            print("\Loss is low so canelling training!")
            self.model.stop_training = True

# call your stupid callback class
callbacks = myCallback()

fashion_mnist=keras.datasets.fashion_mnist
(training_images,training_labels),(test_images,test_labels)=fashion_mnist.load_data()

# Normalize the pixel values of the train and test images, they work better with smaller values.
training_images  = training_images / 255.0
test_images = test_images / 255.0

#   keras.layers.Dnese(128,activation=tf.nn.relu),
#   The hidden layer

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128,activation=tf.nn.relu),
    keras.layers.Dense(10,activation=tf.nn.softmax)
])

model.compile(optimizer = tf.optimizers.Adam(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

# add callback in training process
model.fit(training_images, training_labels, epochs=5,callbacks=[callbacks])

# Evaluate the model on unseen data
model.evaluate(test_images, test_labels)
