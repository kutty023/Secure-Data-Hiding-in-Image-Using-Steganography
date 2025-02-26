import cv2
import numpy as np

def encode_message(image_path, message, password, output_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Image not found")
    
    d = {chr(i): i for i in range(256)}
    n, m, z = 0, 0, 0
    
    for char in password + message:
        img[n, m, z] = d[char]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3
    
    cv2.imwrite(output_path, img)