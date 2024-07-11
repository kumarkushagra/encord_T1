import requests
import json
import os
import numpy as np
from PIL import Image

url = 'http://122.171.130.2:8000/predict'
dicom_directory = r'D:\Panacea\Encord\encord_T1\dataset\DCM files'  # Directory containing DICOM files
dataset_directory = r'D:\Panacea\Encord\encord_T1\dataset'
json_save_directory = os.path.join(dataset_directory, 'JSON_files')
image_save_directory = os.path.join(dataset_directory, 'predicted_mask')

# Create directories if they don't exist
os.makedirs(json_save_directory, exist_ok=True)
os.makedirs(image_save_directory, exist_ok=True)

def convert_boolean_to_integer(obj):
    if isinstance(obj, bool):
        return 1 if obj else 0
    elif isinstance(obj, list):
        return [convert_boolean_to_integer(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: convert_boolean_to_integer(value) for key, value in obj.items()}
    else:
        return obj

# Iterate over all files in the DICOM directory
for filename in os.listdir(dicom_directory):
    dicom_file = os.path.join(dicom_directory, filename)
    
    # Skip if it's not a file
    if not os.path.isfile(dicom_file):
        continue
    
    with open(dicom_file, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)

    if response.status_code == 200:
        json_data = response.json()

        # Save the JSON response with the same name as the DICOM file
        base_filename = os.path.splitext(filename)[0]
        json_path = os.path.join(json_save_directory, f"{base_filename}.json")
        with open(json_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
        print(f"JSON response saved as {json_path}")

        # Convert 'segInfo' values from boolean to integer (True: 1, False: 0)
        if 'segInfo' in json_data:
            seg_info_list = json_data['segInfo']
            
            # Assuming there could be multiple 'segInfo' objects, process each one
            for seg_info in seg_info_list:
                if 'seg' in seg_info:
                    seg_array = np.array(seg_info['seg'], dtype=np.uint8)  # Convert to numpy array

                    # Create PIL image from numpy array
                    img = Image.fromarray(seg_array * 255, mode='L')  # Convert 0/1 to 0/255 for grayscale

                    # Save the image in the predicted_mask directory with the same name as the DICOM file
                    image_path = os.path.join(image_save_directory, f"{base_filename}.jpg")
                    img.save(image_path)

                    print(f"Segmentation image saved as {image_path}")
                else:
                    print("No 'seg' array found in one of the 'segInfo' objects.")
        else:
            print("No 'segInfo' found in JSON response.")
    else:
        print(f"Error: {response.status_code}, {response.text}")
