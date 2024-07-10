import gradio as gr
import numpy as np
from PIL import Image

def annotate_image(mask_image_path: str, prediction_image_path: str, base_image_path: str):
    # Open and convert the mask image to grayscale and then to a numpy array
    mask_image = Image.open(mask_image_path).convert("L")
    mask_array = np.array(mask_image)   
    mask_array = np.where(mask_array < 25, 0, mask_array)

    # Prediction conversion
    prediction_image = Image.open(prediction_image_path).convert("L")
    prediction_array = np.array(prediction_image)   
    prediction_array = np.where(prediction_array < 25, 0, prediction_array)
    
    # Open and convert the base image to a numpy array
    base_image = Image.open(base_image_path).convert("RGB")
    base_image_np = np.array(base_image)

    # Create annotations
    annotations = [(mask_array, "Ground Truth"),(prediction_array,"Prediction")]

    return base_image_np, annotations

# Create Gradio components
image_input = gr.Image(type="filepath", label="Base Image (512x512)")
prediction_input = gr.Image(type="filepath", label="Mask Image (512x512)")
mask_input = gr.Image(type="filepath", label="Mask Image (512x512)")
annotated_image_output = gr.AnnotatedImage(label="Annotated Image")

# Example usage
examples = [
    [r"D:\PROJECT\encord_T1\dataset\mask\481 CT Plain_15.jpg",r"D:\PROJECT\encord_T1\dataset\mask\086 CT 55mm Plain_17.jpg", r"D:\PROJECT\encord_T1\dataset\JPG files\481 CT Plain_15.jpg"]
]

# Define the interface
interface = gr.Interface(
    fn=annotate_image,
    inputs=[mask_input,prediction_input, image_input],
    outputs=annotated_image_output,
    examples=examples,
    live=True
)

# Launch the app
if __name__ == "__main__":
    interface.launch()
