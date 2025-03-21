import streamlit as st
from PIL import Image
import os
from main import get_image_ocr

# Streamlit UI setup
st.title("OCR For Circulars")

# Upload image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# OCR mode selection
ocr_mode = st.selectbox("Select OCR Mode", [1, 2], index = 0, format_func=lambda x: "Plain Text Tesseract" if x == 1 else "Custom HOCR" if x == 2 else f"Mode {x}")

# Language selection
lang = st.text_input("Enter language (e.g., eng+hin)", "eng+hin")

# Process button
if st.button("Run OCR"):
    if uploaded_image is not None:
        # Save the uploaded file temporarily
        image_path = f"temp_image.{uploaded_image.type.split('/')[-1]}"
        with open(image_path, "wb") as f:
            f.write(uploaded_image.getbuffer())

        # Display the uploaded image and OCR response side by side
        image = Image.open(uploaded_image)
        response = get_image_ocr(image_path, ocr_mode, lang)

        col1, col2 = st.columns(2)
        with col1:
            st.image(image, caption="Uploaded Image", use_column_width=True)
        with col2:
            st.write(response)

        # Clean up temporary file
        os.remove(image_path)
    else:
        st.error("Please upload an image first!")