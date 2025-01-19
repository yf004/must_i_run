from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import tensorflow as tf

# Load the pre-trained MobileNetV2 model
model = tf.keras.applications.MobileNetV2(weights='imagenet', include_top=False, pooling='avg')

def preprocess_image(image):
    # Resize and preprocess the image for the model
    image = image.resize((224, 224))  # Resize to the model's input size
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    image_array = tf.keras.applications.mobilenet_v2.preprocess_input(image_array)
    return image_array

def get_feature_vector(image):
    # Get the feature vector for the image
    processed_image = preprocess_image(image)
    feature_vector = model.predict(processed_image)
    return feature_vector

def calculate_similarity(vector1, vector2):
    # Calculate cosine similarity between two feature vectors
    dot_product = np.dot(vector1, vector2.T)
    norm_a = np.linalg.norm(vector1)
    norm_b = np.linalg.norm(vector2)
    similarity = dot_product / (norm_a * norm_b)
    return similarity

def compare_images():
    # Open the images
    img1 = Image.open(static/image/sg.png)
    img2 = Image.open(static/image/classic.png)

    # Get feature vectors
    vector1 = get_feature_vector(img1)
    vector2 = get_feature_vector(img2)

    # Calculate similarity
    similarity = calculate_similarity(vector1, vector2)

    # Define a threshold for matching (this can be adjusted)
    threshold = 0.8  # Adjust this value based on your needs
    match = similarity >= threshold
    temp = jsonify({
        'similarity': float(similarity),
        'match': match
    })
    print(temp)
    return temp

compare_images()