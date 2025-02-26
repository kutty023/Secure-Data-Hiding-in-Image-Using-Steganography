import cv2

def decode_message(image_path, password):
    img = cv2.imread(image_path)
    if img is None:
        return None
    
    c = {i: chr(i) for i in range(256)}
    n, m, z = 0, 0, 0
    extracted_password = ""

    # Extract password to verify
    for _ in range(len(password)):
        extracted_password += c[img[n, m, z]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3
    
    if extracted_password != password:
        return None  # Incorrect password

    # Extract hidden message
    message = ""
    while True:
        char = c[img[n, m, z]]
        if char == '\0' or len(message) > 100:  # Stop if null terminator or limit reached
            break
        message += char
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    return message if message else None
