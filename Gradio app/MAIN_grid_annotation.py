import gradio as gr
import numpy as np
from PIL import Image
from generate_image_array import *

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

def prev_images(index, pairs):
    index = (index - 1) % len(pairs)
    return [annotate_image(index, pairs), index]

def next_images(index, pairs):
    index = (index + 1) % len(pairs)
    return [annotate_image(index, pairs), index]

# Modify this to get the entire array of matching pairs
dir1 = 'D:/PROJECT/encord_T1/dataset/mask'
dir2 = 'D:/PROJECT/encord_T1/dataset/mask'
dir3 = 'D:/PROJECT/encord_T1/dataset/JPG files'
image_triplets = get_image_pairs(dir1, dir2, dir3)
index = 1

with gr.Blocks() as demo:
    with gr.Row():
        annotated_image_output = gr.AnnotatedImage(value=annotate_image(index, image_triplets),
                                                   color_map={"Prediction": "#FF0000", "Ground_Truth": "#0000FF"},
                                                   label="Annotated Image")

    with gr.Row():
        prev_btn = gr.Button("Prev")
        next_btn = gr.Button("Next")

    state = gr.State(index)

    # Update the images on button click
    prev_btn.click(fn=prev_images, inputs=[state, gr.State(image_triplets)], outputs=[annotated_image_output, state])
    next_btn.click(fn=next_images, inputs=[state, gr.State(image_triplets)], outputs=[annotated_image_output, state])

# Launch the app
if __name__ == "__main__":
    demo.launch()
