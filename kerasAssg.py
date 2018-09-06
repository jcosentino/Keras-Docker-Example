import numpy as np
import h5py
import tensorflow as tf
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import sys
from keras import backend as K

file = 'cats_dogs_model.hdf5'

def get_model():
    global model
    model = load_model(file)
    global graph
    graph = tf.get_default_graph()

def createImageTensor(img):
    return tf.keras.preprocessing.image.load_img(
            img,
            grayscale=False,
            target_size=(150,150,3),
            interpolation='nearest')

def createSinglePrediction(img):
    get_model()
    hdf = h5py.File(file)
    x = createImageTensor(img)
    x = np.expand_dims(x, axis=0) #Used for single images
    with graph.as_default():
        prediction = model.predict(x)
        return 'cats' if prediction == 0 else 'dog'