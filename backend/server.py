from flask import Flask, request, send_file, jsonify, make_response
from encrypt import encode_message
from decrypt import decode_message
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

@app.route('/encrypt', methods=['POST'])
def encrypt():
    if 'image' not in request.files or 'password' not in request.form:
        return jsonify({"error": "Image and password required"}), 400
    
    image = request.files['image']
    password = request.form['password']
    message = request.form.get('message', '')

    image_path = os.path.join(UPLOAD_FOLDER, "uploaded_image.png")
    encrypted_path = os.path.join(UPLOAD_FOLDER, "encrypted_image.png")

    image.save(image_path)
    encode_message(image_path, message, password, encrypted_path)
    return send_file(encrypted_path, as_attachment=True)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    if 'image' not in request.files or 'password' not in request.form:
        return jsonify({"error": "Image and password required"}), 400
    image = request.files['image']
    password = request.form['password']
    image_path = os.path.join(UPLOAD_FOLDER, "uploaded_encrypted.png")
    image.save(image_path)
    
    try:
        decrypted_message = decode_message(image_path, password)
        if decrypted_message is None:
            return jsonify({"error": "Incorrect password or no message found"}), 400
        return jsonify({"message": decrypted_message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)