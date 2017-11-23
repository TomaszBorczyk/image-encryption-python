import ast
from image import *
from rsaCrypto import *
from openKeys import *
from generateKeys import *
from keysBase64 import *


decision = input('Generate, Encrypt or decrypt?')
# generate
if decision is 'g':
    generate()
    # loadPubKey()
    # print(loadPublicKey())


if decision is 'e':
    # encrypt
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

if decision is 'd':
    # decrypt
    private = loadPrivateKey()
    encryptedImg = open('test', 'r').read()
    print(encryptedImg)
    decryptedStr = decrypt(int(encryptedImg), private)
    print('asdasd', decryptedStr)
    text = asciiToText(decryptedStr)
    print(text)