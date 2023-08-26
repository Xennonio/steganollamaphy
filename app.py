from flask import Flask, render_template, request, redirect
from PIL import Image

from llamanographer import encryptimg, decryptimg, text_to_binary, image_scale

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('layout.html')


@app.route('/encrypt', methods = ['GET', 'POST'])
def encrypt():
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
        encryptimg(image, 'encrypted_image', binary_message)

        return render_template('encrypted.html')
    else:
        return render_template('encrypt.html')


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