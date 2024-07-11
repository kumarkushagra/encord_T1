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
    mask_array = np.where(mask_array < 25, 0, 1)

    # Prediction conversion
    prediction_image = Image.open(prediction_image_path)
    prediction_array = np.array(prediction_image)
    prediction_array = np.where(prediction_array < 25, 0, 1)

    empty_mask = np.where(prediction_array < 0, 0, 0)
    # Create annotations
    annotations = [(mask_array, "Ground_Truth"), (prediction_array, "Prediction"),(empty_mask,"Base image")]

    return (base_image_path, annotations)
# example = [['D:/PROJECT/encord_T1/dataset/mask/004 CT 5mm_16.jpg', 'dataset/predicted_mask/004 CT 5mm_16.jpg', 'D:/PROJECT/encord_T1/dataset/JPG files/004 CT 5mm_16.jpg']]
# with gr.Blocks() as demo:
#     with gr.Row():
#         label1 = gr.AnnotatedImage(value = annotate_image(example))
# demo.launch()