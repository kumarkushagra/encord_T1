import os
import cv2
import numpy as np

def save_image(image, image_name, directory):
    # Construct the full path to save the image with .jpg extension
    save_path = os.path.join(directory, image_name)
    
    # Save the image as JPG using OpenCV
    cv2.imwrite(save_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    
    # print(f"Image '{image_name}' saved successfully as JPG to '{directory}'.")

# Example usage:
# Assuming 'image' is your cv2 image array, 'image_name' is the filename without extension, and 'directory' is the target directory path.
# save_image_as_jpg(image, 'example_image.jpg', '/path/to/save/directory')
if __name__=="__main__":
    image = np.zeros((512, 512, 3), dtype=np.uint8)
    image_name = "SAMPLE_1"
    directory = "D:/PROJECT/encord_T1/dataset/mask/overlay/mask"
    save_image(image, image_name, directory)
