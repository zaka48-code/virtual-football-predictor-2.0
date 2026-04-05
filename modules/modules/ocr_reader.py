import pytesseract
import cv2
import numpy as np

def read_image(uploaded_file):
    if uploaded_file is None:
        return ""
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    text = pytesseract.image_to_string(img)
    return text
