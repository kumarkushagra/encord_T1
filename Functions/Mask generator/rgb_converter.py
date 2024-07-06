import matplotlib.colors as mcolors



# def hex_to_bgr(hex_code):
#     rgb_color = mcolors.hex2color(hex_code)
#     bgr_color = tuple(reversed([int(255 * x) for x in rgb_color]))  # Reversed order (BGR)
#     return bgr_color # Returns (B,G,R) format [easy for cv2 to use]


def hex_to_rgb(hex_code):
    rgb_color = mcolors.hex2color(hex_code)
    rgb_color = tuple([int(255 * x) for x in rgb_color])  # Convert to RGB format
    return rgb_color  # Returns (R, G, B) format

# Example usage

if __name__=="__main__":
    hex_code = '#808000'
    print(hex_to_rgb(hex_code))  # Output will be in (R, G, B) format


