import numpy as np
import json 
import cv2

from load_json_data import load_json_data
from create_mask import process_annotations







def generate_mask(json_path, Mask_directory):
    # READ JSON FILE
    data = load_json_data(json_path) 
    # data is a list containing 10 dictionaries, each dict contains data about each study

    # Iterating though each study
    for study in data:
        # ENTERING The nested dictionary inside 'data_units' (dict that contains info about all slices + metadata)
        for data_units in study['data_units'].values():
            # Iterating through labels dict (dict that contains info about each slice ONLY)
            for key,instance in data_units['labels'].items():
                image = np.zeros((512, 512, 3), dtype=np.uint8)
                objects= instance['objects']

                print(key)
                if not objects:
                    continue
                elif objects:
                    name = study['data_title']
                    name += f"_{key}.jpg"
                    process_annotations(image,objects)
                    # Pass this object to process annotations function

                    # SAVE the image (specify directory path)
                    output_path = f"D:/PROJECT/encord_T1/dataset/mask/overlay/mask/{name}"
                    cv2.imwrite(output_path, image)
                    # # Display the result image
                    # cv2.imshow('Result', image)
                    # cv2.waitKey(0)
                    # cv2.destroyAllWindows()
            
                




if __name__=="__main__":
    json_path = "D:/PROJECT/encord_T1/signed_Data.json"
    # base_image_directory = to be done after downlaod functionloty is ready
    Mask_directory = "D:/PROJECT/encord_T1/dataset/mask/overlay/"
    generate_mask(json_path, Mask_directory)
