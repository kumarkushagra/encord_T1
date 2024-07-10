import os
from PIL import Image
import re
import gradio as gr

def numerical_sort(value):
    parts = re.split(r'(\d+)', value)
    return [int(part) if part.isdigit() else part for part in parts]

def get_image_pairs(blank_size=(512, 512)):
    dir1 = r'.\dataset\JPG files'
    dir2 = r'.\dataset\mask'

    image_pairs = []

    # List images in both directories and sort them numerically
    images_dir1 = sorted(os.listdir(dir1), key=numerical_sort)
    images_dir2 = sorted(os.listdir(dir2), key=numerical_sort)

    # Generate blank image
    blank_image_path = os.path.join(dir1, "blank_image.png")
    if not os.path.exists(blank_image_path):
        blank_image = Image.new('RGB', blank_size, (0, 0, 0))
        blank_image.save(blank_image_path)
    
    # Find pairs
    all_images = sorted(set(images_dir1).union(set(images_dir2)), key=numerical_sort)
    for img in all_images:
        path1 = os.path.join(dir1, img) if img in images_dir1 else blank_image_path
        path2 = os.path.join(dir2, img) if img in images_dir2 else blank_image_path
        image_pairs.append((path1, path2))

    return image_pairs

def display_image_pair(index, pairs):
    if index < 0:
        index = len(pairs) - 1
    elif index >= len(pairs):
        index = 0
    path1, path2 = pairs[index]
    label1 = f"Original Image: {os.path.basename(path1)}"
    label2 = f"Masked Image: {os.path.basename(path2)}"
    return path1, path2, label1, label2, index

def prev_images(index, pairs):
    index -= 1
    return display_image_pair(index, pairs)

def next_images(index, pairs):
    index += 1
    return display_image_pair(index, pairs)

# Initialize the state
image_pairs = get_image_pairs()
index = 0

# Define the Gradio interface
with gr.Blocks() as demo:
    with gr.Row():
        label1 = gr.Markdown(value=f"Original Image: {os.path.basename(image_pairs[index][0])}")
        label2 = gr.Markdown(value=f"Masked Image: {os.path.basename(image_pairs[index][1])}")

    with gr.Row():
        image1 = gr.Image(value=image_pairs[index][0], label="Original Image")
        image2 = gr.Image(value=image_pairs[index][1], label="Masked Image")
   

    with gr.Row():
        prev_btn = gr.Button("Prev")
        next_btn = gr.Button("Next")
   
    state = gr.State(index)
   
    # Update the images on button click
    prev_btn.click(fn=prev_images, inputs=[state, gr.State(image_pairs)], outputs=[image1, image2, label1, label2, state])
    next_btn.click(fn=next_images, inputs=[state, gr.State(image_pairs)], outputs=[image1, image2, label1, label2, state])
 
# Launch the app
demo.launch()
