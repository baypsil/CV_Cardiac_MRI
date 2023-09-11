import numpy as np

def highlight_classes(image, mask):
    # Define colors for each class
    class_colors = {
        1: 0,    # Right Ventricle
        2: 127.5,    # Myocardium
        3: 255,    # Left Ventricle
    }

    # convert mask labels to integer
    mask = mask.astype(int)

    # Create a new image for visualization
    visualized_image = np.copy(image)

    # Loop through each pixel in the mask
    for row in range(mask.shape[0]):
        for col in range(mask.shape[1]):
            pixel_class = mask[row, col]

            # Check if the pixel class is 0-2
            if pixel_class in class_colors.keys():
                # Get the corresponding color for the class
                color = class_colors[pixel_class]

                # Highlight the pixel in the visualized image
                visualized_image[row, col] = color

    return visualized_image
