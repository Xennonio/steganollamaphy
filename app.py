# Import necessary libraries
from flask import Flask, render_template, request, redirect, session, jsonify
from PIL import Image
import os
import random as rd

# Import cryptography functions from another file
from llamanographer import encryptimg, decryptimg, text_to_binary, random_name_generator

# Create a Flask web application
app = Flask(__name__, static_url_path='/static')

# Define a route for the root URL '/'
@app.route('/')
def index():
    return render_template('homepage.html')

# Define a route for handling POST requests to '/get_image_size'
@app.route('/get_image_size', methods=['POST'])
def get_image_size():
    # Check if a file named 'img' is included in the POST request
    if request.files['img']:
        image = Image.open(request.files['img'])
        image_size = image.size[0] * image.size[1]

        # Return the image size as a JSON response
        return jsonify({'image_size': image_size})
    
    # If no 'img' file is found in the request, return None as the image size
    return jsonify({'image_size': None})

# Define a route for handling both GET and POST requests at '/encrypt'
@app.route('/encrypt', methods = ['GET', 'POST'])
def encrypt():
    # Initialize image_size with a default value (e.g., None) if it doesn't exist in the session
    image_size = session.get('image_size', None)

    # Check if the request method is POST
    if request.method == 'POST':
        # Get the responses from the request
        img_opt = request.form.get('imgatt_opt')
        filename = random_name_generator()
        message = request.form.get('msg')

        if img_opt == 'specify':
            image = Image.open(request.files['img'])
        else:
            default_img = request.form.get('img')
            if default_img == 'img1':
                image = Image.open('./static/default_images/img1.jpg')
            if default_img == 'img2':
                image = Image.open('./static/default_images/img2.jpg')
            if default_img == 'img3':
                image = Image.open('./static/default_images/img3.jpg')

        # parse the files in the static folder
        saved_images = os.listdir('./static')
        num_images = str(len(saved_images))
        # rename the file if there is one with the same name in the static folder
        for image_name in saved_images:
            if filename + '.jpg' == image_name:
                random_number = rd.randint(0, len(filename))
                filename = filename[0:random_number] + num_images + filename[random_number:]

        # Convert the message to binary and encrypt image with the binary message
        binary_message = text_to_binary(message)
        encrypt_check = encryptimg(image, filename, binary_message)

        image_size = image.size[0] * image.size[1]

        # Replace spaces in the filename with '%20' for URLs
        urlname = ''
        for character in filename:
            if character == ' ':
                urlname += '%20'
            else:
                urlname += character

        # Check the result of the encryption
        if encrypt_check:
            return render_template('encrypted.html', name = filename, url = urlname)
        else:
            return redirect('/') # Redirect the user to the root URL in case of encryption failure
    else:
        return render_template('encrypt.html', image_size = image_size)

# Define a route for handling both GET and POST requests at '/decrypt'
@app.route('/decrypt', methods = ['GET', 'POST'])
def decrypt():

    # Check if the request method is POST
    if request.method == 'POST':
        # Get the responses from the request
        image = Image.open(request.files['img'])
        size_option = request.form.get('decrypt_opt')

        if size_option == 'specify':
            textsize = int(request.form.get('textsize'))
        else:
            textsize = image.size[0] * image.size[1]
        
        # Decrypt the image and obtain a temporary message
        tmpmessage = decryptimg(image, textsize)
        # Initialize an empty string to store the decrypted message in characters
        decrypted_message = ''

        # Convert the list of integers in 'tmpmessage' to characters and concatenate them
        for letter in tmpmessage:
            decrypted_message += chr(letter)

        return render_template('decrypted.html', decrypted_message = decrypted_message)
    else:
        return render_template('decrypt.html')
    
# Defines other routes with some explanatory texts

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/encodings')
def encodings():
    return render_template('encodings.html')

@app.route('/htu')
def howtouse():
    return render_template('howtouse.html')