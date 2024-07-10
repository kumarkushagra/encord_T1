from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def image_to_numpy_array(image_path):
    img = Image.open(image_path)
    
    # Convert image to NumPy array
    img_array = np.array(img)
    
    # Apply threshold of 10
    img_array = np.where(img_array < 10, 0, img_array)
    
    return img_array

# Example usage with plotting
image_path = r"D:\PROJECT\encord_T1\dataset\mask\129 CT 55mm Plain_26.jpg"
image_array = image_to_numpy_array(image_path)

# Plotting the image array
plt.figure(figsize=(8, 6))
plt.imshow(image_array, cmap='gray')  # Assuming grayscale image
plt.title('Image Array (Threshold = 10)')
plt.axis('off')
plt.colorbar()
plt.show()

print(f'Shape of the image array: {image_array.shape}')
