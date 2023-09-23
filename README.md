# Steganollamaphy

Steganollamaphy is a simple one-person website done as a final project for <a href="https://cs50.harvard.edu/x/2023/">Harvard University's CS50 Introductory Computer Science</a> 2023 course. The purpose of the project is to allow hiding information in images (practice called <a href="https://en.wikipedia.org/wiki/Steganography">steganography</a>), being able to store from text messages to links, including a link to an image within the image. The program was written entirely in Flask and is being hosted at http://xenonio.pythonanywhere.com by the <a href="https://www.pythonanywhere.com/">PythonAnywhere</a> integrated development environment service.

## How It Works

1. Because it was created entirely in Flask, Steganollamaphy has a main file `app.py` with the python script that defines the routes corresponding to the pages and actions on the site.

2. The `llamanographer.py` file works as an auxiliary library for `app.py` with the main functions used to encrypt images and carry out steganography processes.

3. In the `/templates` folder there are HTML models for each route in `app.py` that will be rendered by Flask through Jinja2. With `/templates/layout.html` being the main structure of the site and all other files being an extension of this.

4. The `/static` folder contains all the photos and icons used on the website, such as the images shown on the page, the default photo options that can be used in encryption, etc.

5. In most codes there are enough comments to understand the encryption and decryption process, but a more detailed explanation can be found on the <a href="http://xenonio.pythonanywhere.com/about">website itself</a>.

## Main Features

* Hide messages in images
  * You can hide any type of message, from links to an entire textbook (as long as your image has enough pixels to contain all the characters) inside any image.
  * You can either specify it by attaching it from your computer or choosing one of the three default options available on the website.
  * After hiding the message in the photo, you can download it to your device.
  * The encrypted images will be saved in the cloud too and, at the end of encryption, a link will be made available to access the photo in high quality, as sending it as a file on certain social networks compresses the image, resulting in loss of information.
* Discover messages in images
  * You can decrypt any possibly hidden message by attaching any image to the website.
  * You can also choose the number of characters you want to decrypt, since for very large images (like the website's standards) the process of decrypting (and also encrypting) the entire image can be time-consuming.
* Explanation of different types of encodings
  * You can see the explanation and formalization of different types of encryption before hiding your image in an image, or even trying to decrypt a message found in another image.
  * There is an explanation of the main types of encodings, such as alphabets, ciphers and substitution.
* You can see more about the site's main features and how to use them on the <a href="http://xenonio.pythonanywhere.com/htu">website itself</a>.

## Directory structure
```
./steganollamaphy
│   .gitignore
│   app.py
│   llamanographer.py
│
├───static
│   │   alpaca.png
│   │   llama.ico
│   │   llama.jpg
│   │   Morse_Code_Chart.png
│   │
│   └───default_images
│           img1.jpg
│           img2.jpg
│           img3.jpg
│
├───templates
│       about.html
│       decrypt.html
│       decrypted.html
│       encodings.html
│       encrypt.html
│       encrypted.html
│       homepage.html
│       howtouse.html
│       layout.html
└───__pycache__
        app.cpython-39.pyc
        llamanographer.cpython-39.pyc
```

#### Video Demo: <YouTube URL>
