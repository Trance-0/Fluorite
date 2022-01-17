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
        if(float(logs.get('accuracy'))>0.998):
            print("\n Reached 99.8% accuracy so cancelling training!")
            self.model.stop_training = True

# GRADED FUNCTION: train_mnist_conv
def train_mnist_conv():
    # Please write your code only where you are indicated.
    # please do not remove # model fitting inline comments.

    # call your stupid callback class
    callbacks = myCallback()
    mnist = tf.keras.datasets.mnist
    (x_train, y_train),(x_test, y_test) = mnist.load_data(path=path)
    # Normalize the pixel values of the train and test images, they work better with smaller values.
    x_train  = x_train / 255.0
    x_test = x_test/ 255.0

    # Reshape the dataset to meet Conv2D requirement
    training_shape=(len(x_train),x_train[0].shape[0],x_train[0].shape[1],1)
    x_train=x_train.reshape(training_shape)
    test_shape=(len(x_test),x_test[0].shape[0],x_test[0].shape[1],1)
    x_test=x_test.reshape(test_shape)

    model = tf.keras.models.Sequential([
        keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)),
        keras.layers.MaxPooling2D(2,2),
        keras.layers.Flatten(),
        keras.layers.Dense(128,activation='relu'),
        keras.layers.Dense(10,activation='softmax')
    ])

    model.summary()
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    # model fitting
    history = model.fit( x_train ,y_train, epochs=10,callbacks=[callbacks])
    # model fitting
    return history.epoch, history.history['acc'][-1]

_, _ = train_mnist_conv()

# Evaluate the model on unseen data
# model.evaluate(test_images, test_labels)