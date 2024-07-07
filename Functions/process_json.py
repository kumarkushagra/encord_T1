import numpy as np
import json 
import cv2
import csv
import os

from load_json_data import load_json_data
from create_mask import process_annotations
from download import *
from update_CSV import append_row_to_csv





def main(json_path,dataset_dir):
    # READ JSON FILE
    os.makedirs(dataset_dir, exist_ok=True)
    data = load_json_data(json_path) 
    # data is a list containing 10 dictionaries, each dict contains data about each study
    csv_file = f"{dataset_dir}/dataset/record.csv"
    if not os.path.exists(csv_file):
        with open(csv_file, 'w', newline='') as file:
            csv.writer(file).writerow(["name", "Dicom path", "JPG path", "Annotations Found" ,"Bleed status", "mask path", "Fracture status", "Fracture Coordinates"])  # Create file with an empty row


    # Iterating though each study
    DCM_dir= f"{dataset_dir}/dataset/DCM files/"
    os.makedirs(DCM_dir, exist_ok=True)
    mask_dir = f"{dataset_dir}/dataset/mask/"
    os.makedirs(mask_dir, exist_ok=True)
    jpg_dir = f"{dataset_dir}/dataset/JPG files/"
    os.makedirs(jpg_dir, exist_ok=True)
    
    for study in data:
        record = [""]*8

        # ENTERING The nested dictionary inside 'data_units' (dict that contains info about all slices + metadata)
        for data_units in study['data_units'].values():
            name = data_units["data_title"]
            record[0]=name

            """
            GENERATING A url ARRAY FOR PARELLEL DOWNLOADING
            uri_array = []
            for key,instance in data_units['labels'].items():
                # Creating an array of URI (for parellel downloading)
                uri_array.append(instance['metadata']['file_uri'])
            """
            
            # Iterating through labels dict (dict that contains info about each slice ONLY)\
            for key,instance in data_units['labels'].items():
                image = np.zeros((512, 512, 3), dtype=np.uint8)
                objects= instance['objects']


                # # Download each DICOM instance here

                ''' DCM file name ready'''
                uri = instance['metadata']['file_uri']
                study_name = study['data_title']
                dcm_name = f"{study_name}_{key}.dcm"
                jpg_name = f"{study_name}_{key}.jpg"
                dcm_name = f"{DCM_dir}{dcm_name}"
                # Downloading here
                download(uri, DCM_dir, dcm_name, jpg_dir, jpg_name)
                record[1]=dcm_name
                record[2]=jpg_name
                

                for annotation in objects:
                    if annotation["name"]=="Bleed":
                        record[4]="True"
                    elif annotation["name"]=="Fracture":
                        record[6]="True"
                        record[7]=list(annotation["boundingBox"].items())

                ###### Downloading MASK (if exists)
                if not objects:
                    record[3]="No"
                    record[4]="False"
                    record[6]="False"
                    
                elif objects:
                    record[3]="Yes"
                    mask_name = study['data_title']
                    mask_name += f"_{key}.jpg"
                    process_annotations(image,objects)
                    # Pass this object to process annotations function

                    # SAVE the image (specify directory path)
                    mask_path_temp = f"{mask_dir}{mask_name}"
                    record[5]=mask_path_temp
                    cv2.imwrite(mask_path_temp, image)

                
                append_row_to_csv(csv_file,record)
                print(f"saved file: {name}_{key}")
                break




                    # # Display the result image
                    # cv2.imshow('Result', image)
                    # cv2.waitKey(0)
                    # cv2.destroyAllWindows()
        break




if __name__=="__main__":
    json_path = "D:/PROJECT/encord_T1/signed_Data.json"
    # base_image_directory = to be done after downlaod functionloty is ready
    dataset_dir = "D:/PROJECT/encord_T1/"
    main(json_path, dataset_dir)
