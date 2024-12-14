import cv2
import numpy as np
from tkinter import Tk, filedialog

# Function to select an image file
def select_image_file():
     root = Tk ()
     root.withdraw()  # Hide the root window
     fille_path = filedialog.askopenfilename(
        filetypes=[("Image Files", ".png;.jpeg;*.jpg")],
        title="Select an Image File"
    )
    return file_path

# Function to apply rotation
def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
    return rotated_image

# Function to apply scaling
def scale_image(image, scale_x, scale_y):
    dimensions = (int(image.shape[1] * scale_x), int(image.shape[0] * scale_y))
    scaled_image = cv2.resize(image, dimensions, interpolation=cv2.INTER_LINEAR)
    return scaled_image

# Function to apply translation
def translate_image(image, tx, ty):
    (h, w) = image.shape[:2]
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    translated_image = cv2.warpAffine(image, translation_matrix, (w, h))
    return translated_image

# Function to apply skewing (shearing)
def skew_image(image, shear_x, shear_y):
    (h, w) = image.shape[:2]
    shear_matrix = np.float32([[1, shear_x, 0], [shear_y, 1, 0]])
    skewed_image = cv2.warpAffine(image, shear_matrix, (w, h))
    return skewed_image
# Main script
if _name_ == "_main_":
    # Select an image file
    image_path = select_image_file()
    if not image_path:
        print ("No file selected. Exiting.")
        exit ()

    # Load the selected image
    image = cv2.imread(image_path)
    if image is None:
        print ("Failed to load the image. Exiting.")
        exit ()

    # Perform transformations
    rotated = rotate_image(image, 30)  # Rotate by 30 degrees
    scaled = scale_image(image, 0.8, 1.2)  # Scale by 0.8x width and 1.2x height
    translated = translate_image(image, 50, 30)  # Translate by (50, 30) pixels
    skewed = skew_image(image, 0.2, 0.1)  # Skew with factors 0.2 (x-axis) and 0.1 (y-axis)

    # Display results
    cv2.imshow("Original Image", image)
    cv2.imshow("Rotated Image", rotated)
    cv2.imshow("Scaled Image", scaled)
    cv2.imshow("Translated Image", translated)
    cv2.imshow("Skewed Image", skewed)

    # Wait for user input and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
