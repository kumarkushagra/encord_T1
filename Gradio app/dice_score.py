import numpy as np
from PIL import Image
import cv2

def dice_score(true_annotations_path, model_predictions_path):
    """
    Calculate the Dice score between two images after converting them to binary masks.

    Parameters:
    true_annotations_path (str): Path to the ground truth image.
    model_predictions_path (str): Path to the predicted image.

    Returns:
    float: Dice coefficient.
    """
    # Load and convert images to numpy arrays
    true_annotations = np.array(Image.open(true_annotations_path))
    model_predictions = np.array(Image.open(model_predictions_path))

    # Check if the dimensions match
    if true_annotations.shape != model_predictions.shape:
        raise ValueError("Input images must have the same dimensions")

    # Convert to binary masks
    true_annotations_bin = np.logical_not(np.any(true_annotations <= 10, axis=-1)).astype(np.uint8) * 255
    model_predictions_bin = np.logical_not(np.any(model_predictions <= 10, axis=-1)).astype(np.uint8) * 255

    # Display binary images
    # cv2.imshow('True Annotations Binary', true_annotations_bin)
    # cv2.imshow('Model Predictions Binary', model_predictions_bin)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Calculate Dice score
    true_annotations_bin = true_annotations_bin.astype(bool)
    model_predictions_bin = model_predictions_bin.astype(bool)
    intersection = np.logical_and(true_annotations_bin, model_predictions_bin).sum()
    union = true_annotations_bin.sum() + model_predictions_bin.sum()

    if union == 0:
        return 1.0

    dice = 2 * intersection / union
    return dice 

# Example usage
true_annotations_path = 'D:/PROJECT/encord_T1/dataset/mask/457 CT 2.55mm_18.jpg'
model_predictions_path = 'D:/PROJECT/encord_T1/dataset/mask/457 CT 2.55mm_17.jpg'

dice = dice_score(true_annotations_path, model_predictions_path)
print(f"DIce Score: {dice}")
