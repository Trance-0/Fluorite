import tensorflow as tf
from tensorflow import keras
from os import path, getcwd, chdir

# DO NOT CHANGE THE LINE BELOW. If you are developing in a local
# environment, then grab mnist.npz from the Coursera Jupyter Notebook
# and place it inside a local folder and edit the path to that location
path = f"{getcwd()}/mnist.npz"

# callback function to cancel traing when reaching specific accuracy.
class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch,logs={}):
        if(logs.get('accuracy')>0.99):
            print("\Accuracy is high so canelling training!")
            self.model.stop_training = True

# GRADED FUNCTION: train_mnist
def train_mnist():
    # Please write your code only where you are indicated.
    # please do not remove # model fitting inline comments.

    # call your stupid callback class
    callbacks = myCallback()
    mnist = tf.keras.datasets.mnist
    (x_train, y_train),(x_test, y_test) = mnist.load_data(path=path)
    # Normalize the pixel values of the train and test images, they work better with smaller values.
    x_train  = x_train / 255.0
    x_test = x_test/ 255.0
    model = tf.keras.models.Sequential([
        keras.layers.Flatten(input_shape=(28,28)),
        keras.layers.Dense(128,activation=tf.nn.relu),
        keras.layers.Dense(10,activation=tf.nn.softmax)
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    # model fitting
    history = model.fit( x_train ,y_train, epochs=10,callbacks=[callbacks])
    # model fitting
    return history.epoch, history.history['acc'][-1]

train_mnist()

# Evaluate the model on unseen data
# model.evaluate(test_images, test_labels)