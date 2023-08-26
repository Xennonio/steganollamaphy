def encryptimg(image, name, message):
    if len(message) > 3 * image.size[0] * image.size[1]:
        print("text too big for the image")
    else:
        counter = 0
        pixels = image.load()
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                tpx = list(pixels[i, j])
                for k in range(3):
                    '''
                    if message[counter] % 2 == 0 and tpx[i] % 2 == 1:
                        tpx[i] -= 1
                    if message[counter] % 2 == 1 and tpx[i] % 2 == 0:
                        tpx[i] += 1
                    '''
                    if message[counter] != tpx[k] % 2:
                        tpx[k] += 2*message[counter] - 1
                    counter += 1
                    if counter == len(message):
                        pixels[i, j] = tuple(tpx)
                        image.save('static/' + name + '.jpg', format = "PNG")
                        return
                pixels[i, j] = tuple(tpx)


def decryptimg(image, size):
    message = []
    tmp = []
    counter = 0
    pixels = image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            for k in range(3):
                tmp.append(pixels[i, j][k] % 2)
                counter += 1
                if counter % 8 == 0:
                    tmpstr = ''
                    for bit in tmp:
                        tmpstr += str(bit)
                    message.append(int(tmpstr, base = 2))
                    tmp = []
                if counter == 8*size:
                    return message
    return message


def text_to_binary(message):
    binary_message = []
    for letter in message:
        bin = format(ord(letter), '08b')
        for bit in bin:
            binary_message.append(int(bit))
    return binary_message
    

'''
def image_scale(image, scale_factor, name):
    new_size = (image.size[0] * scale_factor, image.size[1] * scale_factor)
    image = image.resize(new_size)
    image.save('static/' + name + '.jpg', format = "PNG")
'''