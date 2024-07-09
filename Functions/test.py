# from encord.objects.coordinates import BitmaskCoordinates
# from PIL import Image
# import numpy as np
# import cv2
# from matplotlib import pyplot as plt

# obj = {
#                 "featureHash": "Zr3Z5lde",
#                 "objectHash": "+pYOp4r0",
#                 "name": "Bleed",
#                 "value": "bleed",
#                 "color": "#16406C",
#                 "shape": "bitmask",
#                 "confidence": 1,
#                 "createdBy": "deleted-annotator@noreply.encord.com",
#                 "createdAt": "Thu, 09 Nov 2023 13:32:46 GMT",
#                 "bitmask": {
#                   "rleString": "dVW16h?4N0O2N2`@FV?e0L3N2M2O2M2N2N2M3O001M2O10001O0000O02N10O1O1O01000001O00010O0000000O2O01O010O010O000010O0010O010O10O010O0100O01000O01000O10000O010O10O01000O1000000OO2000O0100O010O10O01000000O100O0010O0100O001O001O1O1O1O10O01O1O00100O1O010O010O1O100O100O00100O10000O1000OO2000O10000N200000000O0100000000000000000O10000000000O100000000000000000000000000000000000000000000000000000O10000O2O00000O1000000O10001O00001O0001O0000000000000002OO00001O01O000001O0010O0002N001O001O010O00010O001O00010O00010O010O10O01O01O01O00010O010O00010O00100O10O01O01O0100000O100000O0100O010O010000O0100O11OO2OO01O010O1000000O100O01000000010O010O02N1O10O2N1N2O2M2N1O2M4M2M3M103Kbif1",
#                   "top": 0,
#                   "left": 0,
#                   "width": 512,
#                   "height": 512
#                 },
#                 "manualAnnotation": True
#               }
# if __name__=="__main__":
#     bmc = BitmaskCoordinates.from_dict(obj)
#     nparr = np.array(bmc)
#     img = Image.fromarray(nparr)

#     plt.imshow(img, interpolation='nearest')
#     plt.show()



# def draw_bitmask(image, color, obj):
    # bmc = BitmaskCoordinates.from_dict(obj)
    # nparr = np.array(bmc)
    # image = Image.fromarray(nparr)

#     plt.imshow(image, interpolation='nearest')
#     plt.show()


import numpy as np
import cv2
import pycocotools.mask as maskUtils
from encord.objects.coordinates import BitmaskCoordinates
from PIL import Image
import numpy as np
import cv2
from matplotlib import pyplot as plt


def draw_bitmask(image, color, rle_string):
    # Decode RLE string to binary mask
    # rle = {"counts": rle_string, "size": [image.shape[0], image.shape[1]]}
    # mask = maskUtils.decode(rle)
    # print(type(mask))





    bmc = BitmaskCoordinates.from_dict(rle_string)
    mask = np.array(bmc)
    # image = Image.fromarray(mask)

    print(type(mask))




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


if __name__=="__main__":
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
    color = (0,255,255)
    
    draw_bitmask(image, color, objects[0])
    # draw_bbox(image,color,boundingBox)
    # Display the result
    cv2.imshow('Result', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    