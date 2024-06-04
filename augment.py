import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras import Input
from sklearn.model_selection import StratifiedShuffleSplit
from PIL import Image
import pandas as pd
import numpy as np
import os


def load_data(data_dir):
    image_paths = []
    for filename in os.listdir(data_dir):
        if filename.endswith('.jpg'):
            image_path = os.path.join(data_dir, filename)
            image_paths.append(image_path)
    return image_paths

def preprocess_images(image_paths, target_size):
    preprocessed_images = []
    
    for image_path in image_paths:
        # Load the image
        image = Image.open(image_path)
        
        # Resize the image
        image = image.resize(target_size)
        
        # Convert the image to a numpy array
        image_array = np.array(image)
        
        # Normalize the pixel values to the range [0, 1]
        image_array = image_array.astype('float32') / 255.0
        
        # Add the preprocessed image to the list
        preprocessed_images.append(image_array)
        
    # Convert the list to a numpy array
    preprocessed_images = np.array(preprocessed_images)
    
    return preprocessed_images

augmentations = [
    tf.keras.layers.RandomRotation(0.2),
    tf.keras.layers.RandomTranslation(0.2, 0.2), 
    tf.keras.layers.RandomBrightness(0.0025)
]

def augment_images(images):
    for augmentation in augmentations:
        if callable(augmentation):
            images = augmentation(images)
        else:
            images = augmentation(images)
    return images

def save_augmented_images(augmented_images, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for i, image in enumerate(augmented_images):
        # Convert the image tensor to a NumPy array
        image_array = image.numpy()
        
        # Convert the image back to the range [0, 255]
        image_array = (image_array * 255).astype('uint8')
        
        # Convert the NumPy array to a PIL Image
        image = Image.fromarray(image_array)
        
        # Save the image in JPG format
        output_path = os.path.join(output_dir, f"{i}.jpg")
        image.save(output_path)
        
# Glavni del
if __name__ == '__main__':
    print("Nalaganje in priprava podatkov")
    train_images = load_data('images')
    
    print("Predpriprava slik")
    target_size = (64, 64)
    train_images = preprocess_images(train_images, target_size)
    
    print("Augmentacija slik")
    augmented_images = augment_images(train_images)
    
    print("Shranjevanje augmentiranih slik")
    output_dir = "augmented_images"
    save_augmented_images(augmented_images, output_dir)
