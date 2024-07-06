import os
import requests
import pydicom
import cv2

def download_and_convert_dicom(uri, DCM_path, DCM_name, JPG_dir, JPG_name):
    # Ensure the download and save paths exist
    os.makedirs(DCM_path, exist_ok=True)
    os.makedirs(JPG_dir, exist_ok=True)

    # Full paths for the saved files
    dicom_file_path = os.path.join(DCM_path, DCM_name)
    jpg_file_path = os.path.join(JPG_dir, JPG_name)
    
    # Download the DICOM file
    response = requests.get(uri)
    response.raise_for_status()  # Raise an error for bad status

    # Save the DICOM file
    with open(dicom_file_path, 'wb') as file:
        file.write(response.content)
    print(f"DICOM file downloaded and saved as {dicom_file_path}")
    
    # Read the DICOM file
    
def convert_dicom_to_jpg(dicom_file_path, jpg_dir, jpg_name):
    # Ensure the JPG directory exists; create if it doesn't
    os.makedirs(jpg_dir, exist_ok=True)

    # Convert DICOM file to JPG
    jpg_file_path = os.path.join(jpg_dir, f"{jpg_name}.jpg")
    dicom2jpg.dicom2jpg(dicom_file_path, jpg_file_path)

    print(f"Converted DICOM file {dicom_file_path} to JPG: {jpg_file_path}")


# Example usage
if __name__ == "__main__":
    uri = "https://storage.googleapis.com/cord-ai-platform.appspot.com/cord-dicoms-prod/dp2Wf2uuRDg2nHa9CAAnEsltU8d2/54ab613d-54d8-43d9-9415-f68cb73c85ea?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=firebase-adminsdk-64w1p%40cord-ai-platform.iam.gserviceaccount.com%2F20240705%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240705T114251Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=142e34ccc02b2c34343c4d42851361214ca999611040b2d015e0bdeb86ee7b11b66199af6bb0c10623c86f1e94ff4765354be7ca7188fd1d7dcf7f2a5be42dae4b7b9eb4df818d65fbe2cd4e4a321e930fd5689d4b468b417cf9b9492986b96add0c59baf4d040be7929542dfff765cf3263cb2688bb067b10bcee7ce7764d029d1c28d124be229a4f93d37c82b5ef54c48f73736f6fc0d4cc9fbfbee976ae7d50b3589ef2828f7aebf13a17d3a017ef6db0d6152013c75a86f6c97217d0d07be2f6b033eb3dc922d4ff6acedf7daff63f7f480004eb12d2c69a41d030199fe6519d23cb963d5cb4e7de2e4ec7f7baac822bef184a4665eb573cd073626c4760"
    DCM_path = "D:/PROJECT/encord_T1/dataset/DCM files"
    DCM_name = "Name_1.dcm"
    JPG_dir = "D:/PROJECT/encord_T1/dataset/JPG files"
    JPG_name = "Name_1.jpg"

    download_and_convert_dicom(uri, DCM_path, DCM_name, JPG_dir, JPG_name)
