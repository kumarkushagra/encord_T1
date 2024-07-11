import gradio as gr
import numpy as np
from PIL import Image
from generate_image_array import *
from return_tuple_for_annotatedImage import annotate_image

def prev_images(index, pairs):
    index = (index - 8) % len(pairs)
    indices = [(index + i) % len(pairs) for i in range(8)]
    annotated_images = [annotate_image(idx, pairs) for idx in indices]
    return annotated_images + [index]

def next_images(index, pairs):
    index = (index + 8) % len(pairs)
    indices = [(index + i) % len(pairs) for i in range(8)]
    annotated_images = [annotate_image(idx, pairs) for idx in indices]
    return annotated_images + [index]

# Modify this to get the entire array of matching pairs
dir1 = 'dataset/mask'
dir2 = 'dataset/predicted_mask'
dir3 = 'dataset/JPG files'
image_triplets = get_image_pairs(dir1, dir2, dir3)
index = 0

with gr.Blocks() as demo:
    with gr.Row():
    # Create the annotated image outputs
        annotated_image_output1 = gr.AnnotatedImage(
            value=annotate_image(index, image_triplets),
            color_map={"Prediction": "#FF0000", "Ground_Truth": "#0000FF","Base image":"#FFFFFF"},
            label="Annotated Image 1"
        )
        annotated_image_output2 = gr.AnnotatedImage(
            value=annotate_image((index + 1) % len(image_triplets), image_triplets),
            color_map={"Prediction": "#FF0000", "Ground_Truth": "#0000FF","Base image":"#FFFFFF"},
            label="Annotated Image 2"
        )
        annotated_image_output3 = gr.AnnotatedImage(
            value=annotate_image((index + 2) % len(image_triplets), image_triplets),
            color_map={"Prediction": "#FF0000", "Ground_Truth": "#0000FF","Base image":"#FFFFFF"},
            label="Annotated Image 3"
        )
        annotated_image_output4 = gr.AnnotatedImage(
            value=annotate_image((index + 3) % len(image_triplets), image_triplets),
            color_map={"Prediction": "#FF0000", "Ground_Truth": "#0000FF","Base image":"#FFFFFF"},
            label="Annotated Image 4"
        )


    with gr.Row():

        annotated_image_output5 = gr.AnnotatedImage(
            value=annotate_image((index + 4) % len(image_triplets), image_triplets),
            color_map={"Prediction": "#FF0000", "Ground_Truth": "#0000FF","Base image":"#FFFFFF"},
            label="Annotated Image 5"
        )
        annotated_image_output6 = gr.AnnotatedImage(
            value=annotate_image((index + 5) % len(image_triplets), image_triplets),
            color_map={"Prediction": "#FF0000", "Ground_Truth": "#0000FF","Base image":"#FFFFFF"},
            label="Annotated Image 6"
        )
        annotated_image_output7 = gr.AnnotatedImage(
            value=annotate_image((index + 6) % len(image_triplets), image_triplets),
            color_map={"Prediction": "#FF0000", "Ground_Truth": "#0000FF","Base image":"#FFFFFF"},
            label="Annotated Image 7"
        )
        annotated_image_output8 = gr.AnnotatedImage(
            value=annotate_image((index + 7) % len(image_triplets), image_triplets),
            color_map={"Prediction": "#FF0000", "Ground_Truth": "#0000FF","Base image":"#FFFFFF"},
            label="Annotated Image 8"
        )
    

    with gr.Row():
        prev_btn = gr.Button("Prev")
        next_btn = gr.Button("Next")

    state = gr.State(index)

    # Update the images on button click
    prev_btn.click(
        fn=prev_images, 
        inputs=[state, gr.State(image_triplets)], 
        outputs=[
            annotated_image_output1, 
            annotated_image_output2, 
            annotated_image_output3, 
            annotated_image_output4, 
            annotated_image_output5, 
            annotated_image_output6, 
            annotated_image_output7, 
            annotated_image_output8, 
            state
        ]
    )
    next_btn.click(
        fn=next_images, 
        inputs=[state, gr.State(image_triplets)], 
        outputs=[
            annotated_image_output1, 
            annotated_image_output2, 
            annotated_image_output3, 
            annotated_image_output4, 
            annotated_image_output5, 
            annotated_image_output6, 
            annotated_image_output7, 
            annotated_image_output8, 
            state
        ]
    )

# Launch the app
if __name__ == "__main__":
    demo.launch()
