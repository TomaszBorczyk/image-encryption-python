import ast
from image import *
from rsaCrypto import *
from openKeys import *
from generateKeys import *
from keysBase64 import *

decision = input('Generate, Encrypt or decrypt?')
# generate keys
if decision is 'g':
    private, public = generateKeys()
    encodeAndSavePrivate(private)
    encodeAndSavePublic(public)

# encrypt
if decision is 'e':
    public = loadPublicKey()
    # image = openImage('images/lena-greyscale-small.png')
    # # image.show()
    # pixels = getPixelArray(image)
    # print(pixels)
    # strImg = str(pixels)
    encryptedImg = encrypt('mondre rzeczy', public)
    print(encryptedImg)

    with open('test', 'w') as outfile:
        outfile.write(str(encryptedImg))

# decrypt
if decision is 'd':
    private = loadPrivateKey()
    encryptedImg = open('test', 'r').read()
    print(encryptedImg)
    decryptedStr = decrypt(int(encryptedImg), private)
    print('asdasd', decryptedStr)
    text = asciiToText(decryptedStr)
    print(text)