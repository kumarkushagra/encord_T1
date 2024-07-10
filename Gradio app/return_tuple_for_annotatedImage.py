import numpy as np
from PIL import Image


def annotate_image(index, path_arr):
    # initilizing the variables 
    mask_image_path = path_arr[index][0]
    prediction_image_path = path_arr[index][1]
    base_image_path = path_arr[index][2]

    # Open and convert the mask image to grayscale and then to a numpy array
    mask_image = Image.open(mask_image_path).convert("L")
    mask_array = np.array(mask_image)
    mask_array = np.where(mask_array < 25, 0, mask_array)

    # Prediction conversion
    prediction_image = Image.open(prediction_image_path).convert("L")
    prediction_array = np.array(prediction_image)
    prediction_array = np.where(prediction_array < 25, 0, prediction_array)

    # Create annotations
    annotations = [(mask_array, "Ground_Truth"), (prediction_array, "Prediction")]

    return (base_image_path, annotations)

