from flask import Flask, render_template, request, redirect, session, jsonify
from PIL import Image

from llamanographer import encryptimg, decryptimg, text_to_binary, image_scale

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('layout.html')


@app.route('/get_image_size', methods=['POST'])
def get_image_size():
    if request.files['img']:
        image = Image.open(request.files['img'])
        image_size = image.size[0] * image.size[1]
        return jsonify({'image_size': image_size})
    return jsonify({'image_size': None})


@app.route('/encrypt', methods = ['GET', 'POST'])
def encrypt():
    # Initialize image_size with a default value (e.g., None) if it doesn't exist in the session
    image_size = session.get('image_size', None)

    if request.method == 'POST':
        if not request.files['img']:
            print('error')
            redirect('/')
        if not request.form.get('msg'):
            print('error')
            redirect('/')

        image = Image.open(request.files['img'])
        message = request.form.get('msg')

        binary_message = text_to_binary(message)
        encrypt_check = encryptimg(image, 'encrypted_image', binary_message)

        image_size = image.size[0] * image.size[1]
        if encrypt_check:
            return render_template('encrypted.html')
        else:
            return redirect('/')
    else:
        return render_template('encrypt.html', image_size=image_size)


@app.route('/decrypt', methods = ['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        if not request.files['img']:
            print('error')
            redirect('/')
        if not request.form.get('textsize'):
            print('error')
            redirect('/')

        image = Image.open(request.files['img'])
        textsize = int(request.form.get('textsize'))
        
        tmpmessage = decryptimg(image, textsize)
        decrypted_message = ''

        for letter in tmpmessage:
            decrypted_message += chr(letter)

        return render_template('decrypted.html', decrypted_message = decrypted_message)
    else:
        return render_template('decrypt.html')
    
@app.route('/about')
def about():
    return render_template('about.html')