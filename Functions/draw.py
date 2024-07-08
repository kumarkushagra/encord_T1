import numpy as np
import cv2
import pycocotools.mask as maskUtils



def draw_bitmask(image, color, rle_string):
    # Decode RLE string to binary mask
    rle = {"counts": rle_string, "size": [image.shape[0], image.shape[1]]}
    mask = maskUtils.decode(rle)
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
    cv2.rectangle(overlay, (x, y), (x+w, y+h), color[:3], thickness=1)
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
    rle_string = "gVY16h?4M3N0e@Il>9QAKm>5RAMm>3SAMm>4QANn>2RANn>3QAMo>b00000001O00001O0000001O0000001O001O0000000000000000000000000001O0O100O2O0O1O100O1O2O0O1O1O1N2O1N2N2NZOaAO\\>4dAL\\>4dALW>8jAHT>9mAGR>9oAGo=:RBFm=:TBFl=9UBGj=8XBHh=7YBIg=5[BKe=4^BJb=4`BKa=3bBL_=OfB0Z=NhB1Z=KjB4X=HjB7a>N3LWmb0MlR]O4M2O3L3N1O00004L4L2N1O2N1O1O010O000000000001N100O1O1O1O1N2O1O1O1M300O100O10000O1O10000000000O10000000000000001O001N101N3Lc[l3"
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