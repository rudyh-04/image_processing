

import numpy as np
import streamlit as st


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
def main():
    st.title("Image Transformation App")

    # Upload an image file
    uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpeg", "jpg"])

    if uploaded_file is not none:
        # load the selected image
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.unit8), cv2.IMREAD_COLOR)
        
        if image is None:
            st.error("Failed to load the image.")
            return

        # Perform transformations
        rotated = rotate_image(image, 30)  # Rotate by 30 degrees
        scaled = scale_image(image, 0.8, 1.2)  # Scale by 0.8x width and 1.2x height
        translated = translate_image(image, 50, 30)  # Translate by (50, 30) pixels
        skewed = skew_image(image, 0.2, 0.1)  # Skew with factors 0.2 (x-axis) and 0.1 (y-axis)

        # Display results
        st.image(image, caption="Original Image", channels="BGR")
        st.image(rotated, caption="Rotated Image", channels="BGR")
        st.image(scaled, caption="Scaled Image", channels="BGR")
        st.image(translated, caption="Translated Image", channels="BGR")
        st.image(skewed, caption="Skewed Image", channels="BGR")

if __name__ == "__main__":
    main()
        
