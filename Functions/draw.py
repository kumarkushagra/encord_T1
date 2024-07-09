import cv2
import pycocotools.mask as maskUtils
from encord.objects.coordinates import BitmaskCoordinates
import numpy as np


def draw_bitmask(image, color, rle_string):
    # Flip the color tupple to match the (R,G,B) format
    # color = color[::-1]
    # PASS ENTIRE DICT HERE
    bmc = BitmaskCoordinates.from_dict(rle_string)
    mask = np.array(bmc)


    alpha = 0.9  # Transparency for the bitmask

    # Ensure the color is in the correct format (B, G, R)
    color = tuple(int(c) for c in color)

    # Create an overlay where the mask is true
    overlay = np.zeros_like(image, dtype=np.uint8)
    overlay[mask == 1] = color

    # Create a mask where the overlay is applied
    mask_indices = mask == 1

    # Blend only the overlay with the original image
    image[mask_indices] = cv2.addWeighted(overlay[mask_indices], alpha, image[mask_indices], 1 - alpha, 0)
    return image

def draw_bbox(image,color, boundingBox):
    alpha = 0.5
    height, width, _ = image.shape
    x = int(boundingBox["x"] * width)
    y = int(boundingBox["y"] * height)
    w = int(boundingBox["w"] * width)
    h = int(boundingBox["h"] * height)
    # Draw the bounding box on the image with transparency
    overlay = image.copy()
    cv2.rectangle(overlay, (x, y), (x+w, y+h), color[:3], thickness=2)
    cv2.addWeighted(overlay, alpha, image, 1 -alpha, 0, image)


# Have not been tested yet (copied from previous work)


def draw_polygon(image,color, polygon_dict):
    alpha = 0.3
    height, width, _ = image.shape
    polygon_points = []
    for i in range(len(polygon_dict)):
        x = int(polygon_dict[str(i)]["x"] * width)
        y = int(polygon_dict[str(i)]["y"] * height)
        polygon_points.append((x, y))
    pts = np.array([polygon_points], dtype=np.int32)
    mask = image.copy()
    cv2.fillPoly(mask, [pts], color[:3])
    cv2.addWeighted(mask, alpha, image, 1 - alpha, 0, image)

def draw_polyline(image,color, polygon_dict):
        alpha = 0.1
        height, width, _ = image.shape
        polygon_points = []
        for i in range(len(polygon_dict)):
            x = int(polygon_dict[str(i)]["x"] * width)
            y = int(polygon_dict[str(i)]["y"] * height)
            polygon_points.append((x, y))
        cv2.polylines(image, [np.array(polygon_points)], isClosed=False, color=color, thickness=2)

def draw_Rbox(image,color, annotations):
    h, w, x, y, theta = annotations["h"], annotations["w"], annotations["x"], annotations["y"], annotations["theta"]

    # Get image dimensions
    img_h, img_w = image.shape[:2]

    # Calculate the center of the rectangle
    center_x, center_y = int(x * img_w), int(y * img_h)

    # Calculate the size of the rectangle
    rect_w, rect_h = int(w * img_w), int(h * img_h)

    # Create the rectangle
    rect = ((center_x, center_y), (rect_w, rect_h), theta)

    # Get the box points and convert them to integers
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    # Draw the rectangle on the image
    cv2.drawContours(image, [box], 0, color, 2)

def draw_keypoint(image,color, keypoint):
    x, y = keypoint["x"], keypoint["y"]

    # Get image dimensions
    img_h, img_w = image.shape[:2]

    # Calculate the position of the keypoint
    center_x, center_y = int(x * img_w), int(y * img_h)

    # Draw the keypoint on the image
    cv2.circle(image, (center_x, center_y), radius=5, color=color, thickness=-1)








if __name__ == "__main__":
    # Generate a simple image
    image = np.zeros((512, 512, 3), dtype=np.uint8)

    # Example RLE string
    rle_string = "dVW16h?4N0O2N2`@FV?e0L3N2M2O2M2N2N2M3O001M2O10001O0000O02N10O1O1O01000001O00010O0000000O2O01O010O010O000010O0010O010O10O010O0100O01000O01000O10000O010O10O01000O1000000OO2000O0100O010O10O01000000O100O0010O0100O001O001O1O1O1O10O01O1O00100O1O010O010O1O100O100O00100O10000O1000OO2000O10000N200000000O0100000000000000000O10000000000O100000000000000000000000000000000000000000000000000000O10000O2O00000O1000000O10001O00001O0001O0000000000000002OO00001O01O000001O0010O0002N001O001O010O00010O001O00010O00010O010O10O01O01O01O00010O010O00010O00100O10O01O01O0100000O100000O0100O010O010000O0100O11OO2OO01O010O1000000O100O01000000010O010O02N1O10O2N1N2O2M2N1O2M4M2M3M103Kbif1"
    boundingBox= {
    "x": 0.5,
    "y": 0.5,
    "w": 0.15,
    "h": 0.15
    }
    # Color (BGR format)
    color = (0, 121, 255)  # Red color

    # Draw the bitmask on the image
    draw_bitmask(image, color, rle_string)
    # draw_bbox(image,color,boundingBox)
    # Display the result
    cv2.imshow('Result', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

############ Orignal bitmask function, find out the reason for error ##################
# def draw_bitmask(image, color, rle_string):
#     # Decode RLE string to binary mask
#     rle = {"counts": rle_string, "size": [image.shape[0], image.shape[1]]}
#     mask = maskUtils.decode(rle)
#     alpha = 0.9  # Transparency for the bitmask

#     # Ensure the color is in the correct format (B, G, R)
#     color = tuple(int(c) for c in color)

#     # Create an overlay where the mask is true
#     overlay = np.zeros_like(image, dtype=np.uint8)
#     overlay[mask == 1] = color

#     # Create a mask where the overlay is applied
#     mask_indices = mask == 1

#     # Blend only the overlay with the original image
#     image[mask_indices] = cv2.addWeighted(overlay[mask_indices], alpha, image[mask_indices], 1 - alpha, 0)
#     return image