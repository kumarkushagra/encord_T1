""" 
    iputs: object: list
           image: jpg (512,512)

    output: mask_IMAGE: jpg (512,512)
"""

import cv2


from rgb_converter import hex_to_rgb
from draw import *


def process_annotations(image, objects):
    # objects is an array containing dictionary

    # itewrating through the array
    for labels in objects:
        # # Coverting color to (R,G,B)
        color = hex_to_rgb( labels["color"])

        if labels["shape"] == "bitmask":
            draw_bitmask(image,color,labels["bitmask"]["rleString"])
        elif labels["shape"] == "bounding_box":
            draw_bbox(image,color,labels["boundingBox"])
        
        # OTHER FUNCTIONS PENDING
        
        elif labels["shape"] == "polygon":
            draw_polygon(image,color,labels["polygon"])
        elif labels["shape"] == "polyline":
            draw_polyline(image,color,labels["polyline"])
        elif labels["shape"] == "keypoint":
            draw_keypoint(image,color,labels["keypoint"])
        elif labels["shape"] == "rotatable_rectangle":
            draw_Rbox(image,color,labels["rotatable_rectangle"])
    



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
            "rleString": "bVW16i?2O0O2K5N2N2N2O001O2N1O1O2N1O2N100O1O001O1O001O1O00010O1O0000001O0001OfNSObCl0]<YO_Cg0^<]OaCd0]<^ObCb0\\<AcC?\\<BdC>[<CfC<Y<EgC<X<DhC<W<EiC;W<EiC;V<FkC9U<GkC9U<GkC9U<GkC9U<GkC9U<GkC9U<GkC9U<GkC9U<FlC:T<FmC9S<FnC:R<EoC;R<CoC=Q<BPD>P<AQD?P<^ORDa0P<]ORDb0o;\\ORDd0P<XORDh0n;XORDh0c=000001O1O001O1O000O101O1O001N101N100O2O1N2N2N2M`]d0Jgb[O2N7C8N2N2M3O0000000000000002N0000000000000000000000000O10000O1O100O100O10000O10000O10000O100O100O100O1O10000O100O1O100001O00000000000000000001O1O1N2N2Nk[`3",
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