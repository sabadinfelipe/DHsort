####################################################################
# DHSort: A CNN model to classify haploid maize seeds
# Allogamous Plant Breeding Lab
# Author: Felipe Sabadin (felipe.sabadin@usp.br)
#####################################################################

# packages
import numpy as np
import pandas as pd
#import PIL
#import PIL.Image
import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array, array_to_img

## image dataset
# load images
images = os.listdir('./dataset/')
#images = [img if img[-1] == 'y']
images = ['./dataset/' + img for img in images]
#random.shuffle(images)

# preparing images
images_input = [img_to_array(load_img(img, target_size=(100,100), interpolation='bicubic')) for img in images]
images_input = np.array(images_input)

# rescaling images
images_input /= 255

## running the model

# loading model
trained_model = keras.models.load_model('model.h5')

# predictions
y_pred = trained_model.predict(images_input)
y_pred = (y_pred > 0.5).astype(np.int)
y_labels = ['D' if y == 0 else 'H' for y in y_pred]

# getting filenames
images_names = [i.split('./dataset/')[1] for i in images]

# saving results
predictions = pd.DataFrame()
predictions.insert(0, 'file_name', images_names, True)
predictions.insert(1, 'phenotype', y_labels, True)
predictions.to_csv('output.csv', index = False)

### EOF ###
