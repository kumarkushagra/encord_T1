# Project Repository

## Structure of this Repo

### Main Components
- **json file**: Configuration and settings file for the project.

- **main.py**: The main script that orchestrates the workflow by calling various functions from the functions directory.

### Functions Directory
Contains all the necessary functions that `main.py` will call.

#### Download Directory
- **download.py**: Script responsible for downloading the required files.
- **rename.py**: Script for renaming files as needed.
- **append_to_csv.py**: Script to append new data to the existing CSV files.

#### Mask Generator Directory
- **py1**: First script for mask generation.
- **py2**: Second script for mask generation.
- **py3**: Third script for mask generation.
- **to be continued**: Placeholder for future additions.

### Dataset Directory
Contains all the datasets and their respective paths.

#### Download Path
- **dicom files dir**: Directory containing the downloaded DICOM files.
- **dicom to jpg files dir**: Directory for storing converted DICOM to JPG files.
- **Mask dir**: Directory containing mask files.

- **mapping.csv**: CSV file containing all the mappings related to the datasets.
