import cv2
from PIL import Image
import numpy as np

def overlay_images(image_path1, alpha=0.5, beta=0.5, gamma=0):
    # Read the images
    
    prediction_image = Image.open(image_path1).convert("L")
    prediction_array = np.array(prediction_image)
    prediction_array = np.where(prediction_array < 25, 0, prediction_array)


    print(type(prediction_array))
    print(prediction_array)
    # Display the result
    cv2.imshow('mask_array', prediction_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image1='D:/PROJECT/encord_T1/dataset/predicted_mask/457 CT 2.55mm_18.jpg'

overlay_images(image1)
