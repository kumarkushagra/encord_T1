import gradio as gr
import os

# Paths to the directories containing the images
dir1 = "D:/PROJECT/encord_T1/dataset/JPG files"
dir2 = "D:/PROJECT/encord_T1/dataset/mask"

# Get list of image filenames from dir1
filenames = sorted(os.listdir(dir1))

# Filter filenames to only those that exist in both directories
valid_filenames = [f for f in filenames if os.path.exists(os.path.join(dir2, f))]

# Current index to keep track of the displayed image
current_index = 0

def get_images(index):
    global current_index
    if 0 <= index < len(valid_filenames):
        current_index = index
    img1 = os.path.join(dir1, valid_filenames[current_index])
    img2 = os.path.join(dir2, valid_filenames[current_index])
    return img1, img2

def next_images():
    if current_index + 1 < len(valid_filenames):
        return get_images(current_index + 1)
    return get_images(current_index)

def prev_images():
    if current_index - 1 >= 0:
        return get_images(current_index - 1)
    return get_images(current_index)

def image_display(idx):
    img_paths = get_images(idx)
    return img_paths[0], img_paths[1]

iface = gr.Interface(
    fn=image_display,
    inputs=None,
    outputs=[gr.Image(type="filepath", label="Image 1"), gr.Image(type="filepath", label="Image 2")],
    live=True
    # capture_session=True
)

iface.launch()
