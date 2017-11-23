import ast
from image import *
from rsaCrypto import *
from openKeys import *
from generateKeys import *

decision = input('Encrypt or decrypt?')
if decision is 'e':
    # encrypt
    public = getPublic()
    # image = openImage('images/lena-greyscale-small.png')
    # # image.show()
    # pixels = getPixelArray(image)
    # print(pixels)
    # strImg = str(pixels)
    encryptedImg = encrypt('Lubie placki', public)
    print(encryptedImg)

    with open('test', 'w') as outfile:
        outfile.write(str(encryptedImg))

if decision is 'd':
    # decrypt
    private = getPrivate()
    encryptedImg = open('test', 'r').read()
    print(encryptedImg)
    decryptedStr = decrypt(int(encryptedImg), private)
    print('asdasd', decryptedStr)
    text = asciiToText(decryptedStr)
    print(text)