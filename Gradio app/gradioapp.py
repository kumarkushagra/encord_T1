import gradio as gr
import os
from PIL import Image

# Set the directories containing your images
left_image_dir = r"D:\Panacea\Encord\encord_T1\dataset\JPG files"
right_image_dir = r"D:\Panacea\Encord\encord_T1\dataset\mask"

#This is the basic structure of gradio app

# Get a sorted list of image file paths for each directory
left_image_files = sorted([os.path.join(left_image_dir, img) for img in os.listdir(left_image_dir) if img.endswith(('png', 'jpg', 'jpeg'))])
right_image_files = sorted([os.path.join(right_image_dir, img) for img in os.listdir(right_image_dir) if img.endswith(('png', 'jpg', 'jpeg'))])

# Function to resize images to fit within a specific size
def resize_image(image_path, size=(600, 600)):
    with Image.open(image_path) as img:
        img.thumbnail(size)
        resized_path = image_path.replace('.jpg', '_resized.jpg').replace('.jpeg', '_resized.jpeg').replace('.png', '_resized.png')
        img.save(resized_path)
        return resized_path

def display_images(left_index, right_index):
    # Ensure the indices are within bounds
    left_index = max(0, min(left_index, len(left_image_files) - 1))
    right_index = max(0, min(right_index, len(right_image_files) - 1))
    
    # Resize and get paths of images
    img1 = resize_image(left_image_files[left_index])
    img2 = resize_image(right_image_files[right_index])
    return img1, img2, left_index, right_index

def next_images(left_index, right_index):
    left_index += 1
    right_index += 1
    if left_index >= len(left_image_files):
        left_index = len(left_image_files) - 1
    if right_index >= len(right_image_files):
        right_index = len(right_image_files) - 1
    return display_images(left_index, right_index)

def prev_images(left_index, right_index):
    left_index -= 1
    right_index -= 1
    if left_index < 0:
        left_index = 0
    if right_index < 0:
        right_index = 0
    return display_images(left_index, right_index)

# Initialize with the first pair of images
img1, img2, left_index, right_index = display_images(0, 0)

# Define the Gradio interface
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            image1 = gr.Image(value=img1, label="Left Image").style(width=600, height=600)
        with gr.Column():
            image2 = gr.Image(value=img2, label="Right Image").style(width=600, height=600)
    
    with gr.Row():
        prev_btn = gr.Button("Prev")
        next_btn = gr.Button("Next")

    left_state = gr.State(left_index)
    right_state = gr.State(right_index)
    
    # Update the images on button click
    prev_btn.click(prev_images, inputs=[left_state, right_state], outputs=[image1, image2, left_state, right_state])
    next_btn.click(next_images, inputs=[left_state, right_state], outputs=[image1, image2, left_state, right_state])

# Launch the app
demo.launch()
