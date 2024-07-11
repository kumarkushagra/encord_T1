import gradio as gr
import numpy as np
from PIL import Image
from generate_image_array import *
from return_tuple_for_annotatedImage import annotate_image

def prev_images(index, pairs):
    index1 = (index - 1) % len(pairs)
    index2 = (index1 - 1) % len(pairs)
    annotated_image_1 = annotate_image(index1, pairs)
    annotated_image_2 = annotate_image(index2, pairs)
    return [annotated_image_1, annotated_image_2, index2]

def next_images(index, pairs):
    index1 = (index + 1) % len(pairs)
    index2 = (index1 + 1) % len(pairs)
    annotated_image_1 = annotate_image(index1, pairs)
    annotated_image_2 = annotate_image(index2, pairs)
    return [annotated_image_1, annotated_image_2, index2]

# Modify this to get the entire array of matching pairs
dir1 = 'dataset/mask'
dir2 = 'dataset/predicted_mask'
dir3 = 'dataset/JPG files'
image_triplets = get_image_pairs(dir1, dir2, dir3)
index = 0

with gr.Blocks() as demo:
    with gr.Row():
        annotated_image_output1 = gr.AnnotatedImage(
            value=annotate_image(index, image_triplets),
            color_map={"Prediction": "#FF0000", "Ground_Truth": "#0000FF"},
            label="Annotated Image 1"
        )
        annotated_image_output2 = gr.AnnotatedImage(
            value=annotate_image((index + 1) % len(image_triplets), image_triplets),
            color_map={"Prediction": "#FF0000", "Ground_Truth": "#0000FF"},
            label="Annotated Image 2"
        )

    with gr.Row():
        prev_btn = gr.Button("Prev")
        next_btn = gr.Button("Next")

    state = gr.State(index)

    # Update the images on button click
    prev_btn.click(fn=prev_images, inputs=[state, gr.State(image_triplets)], outputs=[annotated_image_output1, annotated_image_output2, state])
    next_btn.click(fn=next_images, inputs=[state, gr.State(image_triplets)], outputs=[annotated_image_output1, annotated_image_output2, state])

# Launch the app
if __name__ == "__main__":
    demo.launch()
