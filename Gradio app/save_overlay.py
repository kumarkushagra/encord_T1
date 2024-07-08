import cv2

def overlay_images(image_path1, image_path2, alpha=0.5, beta=0.5, gamma=0):
    # Read the images
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)
    
    # Check if images are loaded properly
    if image1 is None:
        print(f"Error loading image1 from {image_path1}")
        return
    if image2 is None:
        print(f"Error loading image2 from {image_path2}")
        return
    
    # Resize image2 to match image1 dimensions if necessary
    if image1.shape != image2.shape:
        image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
    
    # Overlay the images
    overlay = cv2.addWeighted(image1, alpha, image2, beta, gamma)
    
    # Display the result
    cv2.imshow('Overlay', overlay)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image1='D:/PROJECT/encord_T1/dataset/mask/457 CT 2.55mm_18.jpg'
image2='D:/PROJECT/encord_T1/dataset/mask/457 CT 2.55mm_17.jpg'
overlay_images(image1,image2)
