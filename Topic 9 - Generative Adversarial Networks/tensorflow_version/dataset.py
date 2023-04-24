import glob
import imageio
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os
import PIL
import time


def setup_dataset(buffer_size, batch_size):
    (train_images, train_labels), (_, _) = tf.keras.datasets.fashion_mnist.load_data()
    train_images = train_images.reshape(train_images.shape[0], 28, 28, 1).astype('float')
    train_images = (train_images - 127.5) / 127.5

    train_dataset = tf.data.Dataset.from_tensor_slices(train_images).shuffle(buffer_size).batch(batch_size)
    return train_dataset