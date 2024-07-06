import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut, apply_modality_lut
import numpy as np
from PIL import Image
import os

# Code copied from "https://github.com/ykuo2/dicom2jpg/blob/main/dicom2jpg/utils.py"

def convert_dicom_to_jpg(dicom_slice_path, jpg_dir, jpg_name):
    # Read the DICOM file
    ds = pydicom.dcmread(dicom_slice_path)
    
    # Get pixel array from the DICOM file
    pixel_array = ds.pixel_array.astype(float)

    # Apply modality LUT if available
    if 'RescaleSlope' in ds and 'RescaleIntercept' in ds:
        rescale_slope = float(ds.RescaleSlope)
        rescale_intercept = float(ds.RescaleIntercept)
        pixel_array = pixel_array * rescale_slope + rescale_intercept
    else:
        pixel_array = apply_modality_lut(pixel_array, ds)
    
    # Apply VOI LUT if available
    if 'VOILUTFunction' in ds and ds.VOILUTFunction == 'SIGMOID':
        pixel_array = apply_voi_lut(pixel_array, ds)
    elif 'WindowCenter' in ds and 'WindowWidth' in ds:
        window_center = ds.WindowCenter
        window_width = ds.WindowWidth
        if isinstance(window_center, pydicom.multival.MultiValue):
            window_center = float(window_center[0])
        else:
            window_center = float(window_center)
        if isinstance(window_width, pydicom.multival.MultiValue):
            window_width = float(window_width[0])
        else:
            window_width = float(window_width)
        pixel_array = _get_LUT_value_LINEAR_EXACT(pixel_array, window_width, window_center)
    else:
        pixel_array = apply_voi_lut(pixel_array, ds)
    
    # Normalize the pixel array to the range [0, 255]
    pixel_array = (pixel_array - pixel_array.min()) / (pixel_array.max() - pixel_array.min()) * 255.0
    
    # Invert the image if the Photometric Interpretation is MONOCHROME1
    if 'PhotometricInterpretation' in ds and ds.PhotometricInterpretation == "MONOCHROME1":
        pixel_array = np.max(pixel_array) - pixel_array
    
    # Convert to uint8
    pixel_array = pixel_array.astype(np.uint8)
    
    # Create a PIL image from the normalized pixel array
    image = Image.fromarray(pixel_array)
    
    # Ensure the jpg_dir exists
    if not os.path.exists(jpg_dir):
        os.makedirs(jpg_dir)
    
    # Save the image as a JPG file
    jpg_path = os.path.join(jpg_dir, jpg_name)
    image.save(jpg_path, 'JPEG')

def _get_LUT_value_LINEAR_EXACT(data, window, level):
    data_min = data.min()
    data_max = data.max()
    data_range = data_max - data_min
    data = np.piecewise(data, 
                        [data <= (level - (window) / 2), 
                         data > (level + (window) / 2)], 
                        [data_min, data_max, lambda data: ((data - level + window / 2) / window * data_range) + data_min])
    return data

if __name__ == "__main__":
    dicom_file_path = 'D:/PROJECT/encord_T1/dataset/DCM files/Name_1.dcm'
    jpg_dir = 'D:/PROJECT/encord_T1/dataset/JPG files/'
    jpg_name = 'test.jpg'
    convert_dicom_to_jpg(dicom_file_path, jpg_dir, jpg_name)
