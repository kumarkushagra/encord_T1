import pandas as pd
import numpy as np
import cv2
import os
import csv


def dice_score(image_path1, image_path2):
    # Print the names of the images
    name = os.path.basename(image_path1)

    image_path1 = image_path1.replace('\\', '/')
    image_path2 = image_path2.replace('\\', '/')
    # Read the images
    img1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)

    # Convert images to binary
    _, binary_img1 = cv2.threshold(img1, 10, 255, cv2.THRESH_BINARY)
    _, binary_img2 = cv2.threshold(img2, 30, 255, cv2.THRESH_BINARY)
    
    # Convert binary images to binary arrays
    binary_array1 = binary_img1 // 255  # This will convert the image to 0s and 1s
    binary_array2 = binary_img2 // 255  # This will convert the image to 0s and 1s

    # # Display the binary images
    # display_img1 = binary_array1 * 255
    # display_img2 = binary_array2 * 255
    # cv2.imshow('Binary Image 1', display_img1)
    # cv2.imshow('Binary Image 2', display_img2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    binary_array1 = binary_array1.astype(bool)
    binary_array2 = binary_array2.astype(bool)
    intersection = np.logical_and(binary_array1, binary_array2).sum()
    union = binary_array1.sum() + binary_array2.sum()
    if union == 0:
        return 1.0, name

    dice_score = 2 * intersection / union
    return dice_score , name

if __name__ == "__main__":  
    
    # Define directories
    mask_dir = "D:/PROJECT/encord_T1/dataset/mask"
    predicted_mask_dir = "D:/PROJECT/encord_T1/dataset/predicted_mask"

    # Get sorted file lists with full paths
    files1 = sorted([os.path.normpath(os.path.join(mask_dir, f)) for f in os.listdir(mask_dir) if os.path.isfile(os.path.join(mask_dir, f))])
    files2 = sorted([os.path.normpath(os.path.join(predicted_mask_dir, f)) for f in os.listdir(predicted_mask_dir) if os.path.isfile(os.path.join(predicted_mask_dir, f))])

    # Create pairs of corresponding files with full paths
    pairs = [[files1[i], files2[i]] for i in range(len(files1))]

    # Display the result
    print(pairs[0])
    # Creating CSV if not present
    filename = 'Dice_scores.csv'
    header = ['File name', 'Dice score']
    # Check if the file exists
    if not os.path.isfile(filename):
        # File doesn't exist, create a new CSV with headers
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
        


    for img1 , img2 in pairs:
        score , name= dice_score(img1, img2)
        print(score,name)
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name,score])