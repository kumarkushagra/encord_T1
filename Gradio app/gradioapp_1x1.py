import gradio as gr
import numpy as np
from PIL import Image
from generate_image_array import *
from return_tuple_for_annotatedImage import annotate_image


def prev_images(index, pairs):
    index = (index - 1) % len(pairs)
    annotated_image = annotate_image(index, pairs)
    return [annotated_image, index]

def next_images(index, pairs):
    index = (index + 1) % len(pairs)
    annotated_image = annotate_image(index, pairs)
    return [annotated_image, index]

# Modify this to get the entire array of matching pairs
dir1 = 'D:/PROJECT/encord_T1/dataset/mask'
dir2 = 'D:/PROJECT/encord_T1/dataset/mask'
dir3 = 'D:/PROJECT/encord_T1/dataset/JPG files'
image_triplets = get_image_pairs(dir1, dir2, dir3)
index = 0

with gr.Blocks() as demo:
    with gr.Row():
        annotated_image_output1 = gr.AnnotatedImage(
            value=annotate_image(index, image_triplets),
            color_map={"Prediction": "#FF0000", "Ground_Truth": "#0000FF"},
            label="Annotated Image 1"
        )


    with gr.Row():
        prev_btn = gr.Button("Prev")
        next_btn = gr.Button("Next")

    state = gr.State(index)

    # Update the images on button click
    prev_btn.click(fn=prev_images, inputs=[state, gr.State(image_triplets)], outputs=[annotated_image_output1, state])
    next_btn.click(fn=next_images, inputs=[state, gr.State(image_triplets)], outputs=[annotated_image_output1, state])

# Launch the app
if __name__ == "__main__":
    demo.launch()
