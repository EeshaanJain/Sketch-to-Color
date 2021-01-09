import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import preprocessing

def return_file_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    return file_path


def generate_image(model, image):
    pred = model(image, training=True)
    plt.figure(figsize=(15, 15))
    image_ = tf.squeeze(image)
    pred_  = tf.squeeze(pred)
    display_list = [image_, pred_]
    title = ['Input Image', 'Predicted Image']
    for i in range(2):
        plt.subplot(1,2, i+1)
        plt.title(title[i])
        plt.imshow(display_list[i]*0.5 + 0.5)
        plt.axis('off')
    plt.show()


print('\n')
print('Please select the sketch of the image you want colorized!')
print('=========================================================')
file_path = return_file_path()
image = preprocessing.test_image(file_path)
image = tf.expand_dims(image, axis=0)
model = tf.keras.models.load_model('model')

generate_image(model, image)
