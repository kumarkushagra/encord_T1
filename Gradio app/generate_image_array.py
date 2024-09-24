import os
import re
from PIL import Image
# import json

# def store_nested_array_to_json(json_file_path, nested_array):
#     try:
#         with open(json_file_path, 'w') as json_file:
#             json.dump(nested_array, json_file, indent=4)
#         print(f"Nested array successfully stored in {json_file_path}")
#     except IOError:
#         print(f"Error writing to {json_file_path}")

def numerical_sort(value):
    # Extracts numbers from the string and returns them for sorting
    numbers = re.findall(r'\d+', value)
    return [int(num) for num in numbers]

def create_black_image(path, size=(512, 512)):
    # Creates a black image of specified size
    if not os.path.exists(path):
        black_image = Image.new('RGB', size, (0, 0, 0))
        black_image.save(path)

def get_image_pairs(dir1, dir2, dir3, placeholder_path='black_image.jpg'):
    # Create a black image placeholder if it doesn't exist
    create_black_image(placeholder_path)
    
    # List all files in the directories and sort them numerically
    files1 = sorted(os.listdir(dir1), key=numerical_sort)
    
    # Create the nested array with paths from all three directories
    output_array = []
    for f in files1:
        path1 = os.path.join(dir1, f).replace("\\", "/")
        path2 = os.path.join(dir2, f).replace("\\", "/") if f in os.listdir(dir2) else placeholder_path.replace("\\", "/")
        path3 = os.path.join(dir3, f).replace("\\", "/") if f in os.listdir(dir3) else placeholder_path.replace("\\", "/")
        output_array.append([path1, path2, path3])
    
    return output_array

    # Example usage
if __name__=="__main__":
    dir1 = 'D:/PROJECT/encord_T1/dataset/mask'
    dir2 = 'D:/PROJECT/encord_T1/dataset/predicted_mask'
    dir3 = 'D:/PROJECT/encord_T1/dataset/JPG files'
    output_array = get_image_pairs(dir1, dir2, dir3)

    # print(output_array)
    for triplet in output_array:
        print(triplet)
    # json_file_path="D:/result.json"
    # store_nested_array_to_json(json_file_path, output_array)