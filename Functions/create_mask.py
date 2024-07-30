""" 
    iputs: object: list
           image: jpg (512,512)

    output: mask_IMAGE: jpg (512,512)
"""

import cv2
from encord.objects.coordinates import BitmaskCoordinates
from PIL import Image
import numpy as np
import cv2
from matplotlib import pyplot as plt

from .rgb_converter import hex_to_rgb
from .draw import *


def process_annotations(image, objects):
    # objects is an array containing dictionary

    # itewrating through the array
    for labels in objects:
        # # Coverting color to (R,G,B)
        color = hex_to_rgb( labels["color"])

        if labels["shape"] == "bitmask":
            draw_bitmask(image,color,labels["bitmask"])
        # elif labels["shape"] == "bounding_box":
        #     draw_bbox(image,color,labels["boundingBox"])
        
        # # OTHER FUNCTIONS PENDING
        
        # elif labels["shape"] == "polygon":
        #     draw_polygon(image,color,labels["polygon"])
        # elif labels["shape"] == "polyline":
        #     draw_polyline(image,color,labels["polyline"])
        # elif labels["shape"] == "keypoint":
        #     draw_keypoint(image,color,labels["keypoint"])
        # elif labels["shape"] == "rotatable_rectangle":
        #     draw_Rbox(image,color,labels["rotatable_rectangle"])
    



if __name__ == "__main__":
    image = np.zeros((512, 512, 3), dtype=np.uint8)  # Create a blank image
    objects = [
    {
        "featureHash": "Zr3Z5lde",
        "objectHash": "flumIRVR",
        "name": "Bleed",
        "value": "bleed",
        "color": "#16406C",
        "shape": "bitmask",
        "confidence": 1,
        "createdBy": "deleted-annotator@noreply.encord.com",
        "createdAt": "Thu, 09 Nov 2023 13:39:12 GMT",
        "bitmask": {
            "rleString": "dVW16h?4N0O2N2`@FV?e0L3N2M2O2M2N2N2M3O001M2O10001O0000O02N10O1O1O01000001O00010O0000000O2O01O010O010O000010O0010O010O10O010O0100O01000O01000O10000O010O10O01000O1000000OO2000O0100O010O10O01000000O100O0010O0100O001O001O1O1O1O10O01O1O00100O1O010O010O1O100O100O00100O10000O1000OO2000O10000N200000000O0100000000000000000O10000000000O100000000000000000000000000000000000000000000000000000O10000O2O00000O1000000O10001O00001O0001O0000000000000002OO00001O01O000001O0010O0002N001O001O010O00010O001O00010O00010O010O10O01O01O01O00010O010O00010O00100O10O01O01O0100000O100000O0100O010O010000O0100O11OO2OO01O010O1000000O100O01000000010O010O02N1O10O2N1N2O2M2N1O2M4M2M3M103Kbif1",
            "top": 0,
            "left": 0,
            "width": 512,
            "height": 512
        },
        "manualAnnotation": True
    },
    {
        "featureHash": "pf7KWJd2",
        "objectHash": "L3KRgrwg",
        "name": "Fracture",
        "value": "fracture",
        "color": "#D33115",
        "shape": "bounding_box",
        "confidence": 1,
        "createdBy": "deleted-annotator@noreply.encord.com",
        "createdAt": "Fri, 10 Nov 2023 11:52:48 GMT",
        "manualAnnotation": True,
        "boundingBox": {
            "x": 0.2248,
            "y": 0.4778,
            "w": 0.0181,
            "h": 0.0262
        }
    }
    ]
    
    process_annotations(image, objects)  # Process annotations on a copy of the image

    # Display the result image
    cv2.imshow('Result', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()