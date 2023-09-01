import re

def encryptimg(image, name, message):
    # Check if the length of the message fits the image
    if len(message) > 3 * image.size[0] * image.size[1]:
        print("text too big for the image")
        return False
    else:
        counter = 0  # Initialize a counter to keep track of message bits processed
        pixels = image.load() # Load the pixel data of the image

        # Loop through the image pixels
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                tpx = list(pixels[i, j]) # Get the RGB values of the current pixel

                # Loop through the RGB channels (red, green, blue)
                for k in range(3):
                    # Check if the current message bit is different from the least significant bit of the pixel channel
                    if message[counter] != tpx[k] % 2:
                        # Modify the pixel channel to hide the message bit
                        tpx[k] += 2*message[counter] - 1 # Ensures the pixel channel is even or odd depending on the message bit
                    counter += 1 # Move to the next message bit

                    # Check if all message bits have been processed
                    if counter == len(message):
                        pixels[i, j] = tuple(tpx) # Update the pixel with modified values
                        image.save('static/' + name + '.jpg', format = "PNG") # Save the modified image
                        return True # Return True to indicate successful encryption
                pixels[i, j] = tuple(tpx) # Update the pixel with modified values


def decryptimg(image, size):
    # Initialize empty var to store:
    message = [] # decrypted msg
    tmp = [] # each unicode character in binary
    counter = 0 # keep track of processed bits
    pixels = image.load() # Load the pixel data of the image

    # Loop through the image pixels
    for i in range(image.size[0]):
        for j in range(image.size[1]):

            # Iterate through the RGB channels (red, green, blue)
            for k in range(3):
                # Get the least significant bit of the pixel channel
                tmp.append(pixels[i, j][k] % 2)
                counter += 1

                # Check if a byte (unicode character) have been collected
                if counter % 8 == 0:
                    tmpstr = ''
                    for bit in tmp:
                        tmpstr += str(bit) # Convert the byte to string
                    message.append(int(tmpstr, base = 2)) # Convert the byte to binary
                    tmp = [] # Reset the temporary byte list

                # Check if the total number of bits processed equals the expected size
                if counter == 8*size:
                    return message # Return the decrypted message as a list of bytes
    return message


def text_to_binary(message):
    binary_message = [] # Initialize an empty list to store each bit of the message
    
    # Iterate through each character in the input message
    for letter in message:
        bin = format(ord(letter), '08b') # Convert the character to its 8-bit binary representation

        # Iterate through each bit in the binary representation
        for bit in bin:
            binary_message.append(int(bit)) # store in binary message list
    return binary_message

def replace(message, find, replace, casesensitivity):
    if casesensitivity == 'No':
        compiled = re.compile(re.escape(find), re.IGNORECASE)
        message = compiled.sub(replace, message)
    else:
        message = message.replace(find, replace)

    return message