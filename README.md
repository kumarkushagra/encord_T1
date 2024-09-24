# Project Repository

## Structure of this Repo

### Main Components
- **json file**: Configuration and settings file for the project.

- **main.py**: The main script that orchestrates the workflow by calling various functions from the functions directory. (This is still incomplete)

- **Make sure that in `functions` directory, `process_json` has been executed and then, run the `gradioapp_2x4.py` in dir == `Gradio app`**

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

## Directory Structure

The directory structure for this repository should be organized as follows:

```
project-root/
│
├── json file
├── main.py
│
├── functions/
│   ├── download/
│   │   ├── download.py
│   │   ├── rename.py
│   │   └── append_to_csv.py
│   │
│   └── mask_generator/
│       ├── py1.py
│       ├── py2.py
│       ├── py3.py
│       └── to_be_continued/
│   
│
├── dataset/
│   ├── download_path/
│   │   ├── dicom_files_dir/
│   │   ├── dicom_to_jpg_files_dir/
│   │   └── mask_dir/
│   │
│   └── mapping.csv
```
