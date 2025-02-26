# Secure Data Hiding in Images Using Steganography

## [Output]()
### [Frontend Deployed link]()
### [Backend Deployed link](https://secure-data-hiding-in-image-using.onrender.com) 
## Note : Render will take some time to load (55sec) please do wait and then check the application


## About the Project

This project provides a secure method to hide and retrieve messages within images using steganography. It enables users to encrypt text messages inside images using a password and later decrypt them using the same password. The implementation includes both frontend and backend components to facilitate seamless encryption and decryption.

## Applications

- Secure Communication: Allows confidential data sharing through images.
- Data Privacy: Protects sensitive information by embedding it inside an image.
- Stealth Messaging: Enables hidden message transmission without raising suspicion.
- Forensics & Digital Watermarking: Can be used for watermarking and forensics to track and secure digital content.

## Methods Used

- LSB Steganography: Hides messages in images by modifying the least significant bits of pixel values.

- Algorithms: The message and password are embedded into the least significant bits of image pixels, ensuring minimal perceptual changes.

## Technologies Used
- Frontend: HTML, CSS, JavaScript for user interface.
- Backend: Python (Flask) for handling encryption and decryption requests.

- Libraries Used:
    -   OpenCV (cv2) for image processing.
    -   NumPy for handling numerical operations on images.
    - Flask for setting up a REST API to process image encryption and decryption.
    - Flask-CORS for handling cross-origin requests.

## Installation Guide
Follow these steps to set up and run the project on your local machine:

1. Install Prerequisites
    Ensure you have Python installed on your system. You can download it from python.org.

2. Clone the Repository
    git clone https://github.com/your-repo/steganography-project.git
    cd steganography-project

3. Set Up a Virtual Environment (Optional but Recommended)
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4. Install Dependencies
    pip install -r requirements.txt

5. Start the Backend Server
    python server.py

6. Open the Frontend
    Simply open index.html in a web browser to use the UI for encryption and decryption.

## Usage Guide

### Encryption:
- Click on the Encrypt button.
- Upload an image.
- Enter the secret message and a password.
- Click Encrypt Image to generate a stego image with the hidden message.
- The encrypted image will be downloaded automatically.

### Decryption:
- Click on the Decrypt button.
- Upload the encrypted image.
- Enter the correct password.
- Click Decrypt Image to retrieve the hidden message.

## Notes
- Make sure to remember the password used for encryption, as it's required for decryption.
- Ensure OpenCV and Flask are properly installed to avoid runtime errors.
- If the server is not reachable, check if the Flask server is running properly.