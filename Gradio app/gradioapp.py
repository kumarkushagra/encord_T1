import gradio as gr
import os
from PIL import Image

# Set the directories containing your images
original_image_dir = r"D:\Panacea\Encord\encord_T1\dataset\JPG files"
masked_image_dir = r"D:\Panacea\Encord\encord_T1\dataset\mask"

# Get sorted lists of image file names from each directory
original_images = sorted([img for img in os.listdir(original_image_dir) if img.endswith(('png', 'jpg', 'jpeg'))])
masked_images = sorted([img for img in os.listdir(masked_image_dir) if img.endswith(('png', 'jpg', 'jpeg'))])

# Function to resize images to fit within a specific size
def resize_image(image_path, size=(600, 600)):
    with Image.open(image_path) as img:
        img.thumbnail(size)
        resized_path = image_path.replace('.jpg', '_resized.jpg').replace('.jpeg', '_resized.jpeg').replace('.png', '_resized.png')
        img.save(resized_path)
        return resized_path

def create_black_image(size=(600, 600)):
    black_image = Image.new("RGB", size, (0, 0, 0))
    black_image_path = "black_image.jpg"
    black_image.save(black_image_path)
    return black_image_path

def display_images(index):
    # Ensure the index is within bounds
    index = max(0, min(index, len(original_images) - 1))
    
    # Paths to the original and masked images
    original_image_path = os.path.join(original_image_dir, original_images[index])
    masked_image_path = os.path.join(masked_image_dir, original_images[index])
    
    # Resize original image
    original_img = resize_image(original_image_path)
    
    # Check if the masked image exists and resize it, or create a black image
    if os.path.exists(masked_image_path):
        masked_img = resize_image(masked_image_path)
    else:
        masked_img = create_black_image()
    
    return original_img, masked_img, index

def next_images(index):
    index += 1
    if index >= len(original_images):
        index = len(original_images) - 1
    return display_images(index)

def prev_images(index):
    index -= 1
    if index < 0:
        index = 0
    return display_images(index)

# Initialize with the first pair of images
original_img, masked_img, index = display_images(0)

# Define the Gradio interface
with gr.Blocks() as demo:
    with gr.Row():
        image1 = gr.Image(value=original_img, label="Original Image").style(width=600, height=600)
        image2 = gr.Image(value=masked_img, label="Masked Image").style(width=600, height=600)
    
    with gr.Row():
        prev_btn = gr.Button("Prev")
        next_btn = gr.Button("Next")

    state = gr.State(index)
    
    # Update the images on button click
    prev_btn.click(prev_images, inputs=state, outputs=[image1, image2, state])
    next_btn.click(next_images, inputs=state, outputs=[image1, image2, state])

# Launch the app
demo.launch()
