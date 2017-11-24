import ast
import base64
import numpy as np
from image import *
from rsaCrypto import *
from openKeys import *
from generateKeys import *
from keysBase64 import *
from PIL import Image


decision = input('Generate, Encrypt or decrypt?')
if decision is 'q':

    # png beda przechowywane w taki sposob
    with open('images/lena-greyscale-small.png', "rb") as imageFile:
        s = base64.b64encode(imageFile.read())
        print(s)

    with open('images/new.png', "wb") as imageFile:
        imageFile.write(base64.b64decode(s))

    # fh = open('images/new.png', "wb")
    # fh.write(s.decode('base64'))
    # fh.close()

    # with open('images/lena-greyscale-small.png', 'rb') as imageFile:
    #     s = imageFile.read()
    #     print(s)

    # z = s.decode('unicode_escape').encode('utf-8')
    # print(z)
    # # f = z.decode('utf8').encode('unicode_escape').decode('utf-8').encode('utf-8')
    # f = z.decode('utf8').encode('unicode_escape')
    # print(f)
    # with open('images/new.png', 'wb') as imageFile:
    #     imageFile.write(f)
    
    # image = openImage('images/lena-greyscale-small.png')
    # bts = getBytes(image)
    # img2 = Image.frombytes('PNG', (10, 10), bts)
    # img2.show()
    # print(getBytes(image))

if decision is 's':
    encrypted = open('encryptedimg', 'r').read()
    print(encrypted)
    print(encrypted.split('\n'))

if decision is 'a':
    image = openImage('images/lena-greyscale-small.png')
    image.show()
    with open('images/lena-greyscale-small.png', 'rb') as imageFile:
        msg = imageFile.read()
    # pixels = str(getPixelArray(image))
    # msg = 'RazDwaTrzy'
    # print('pixels', pixels)
    # msg = getBytes(image).decode("utf-8") 
    # print(msg)
    public = loadPublicKey()
    print('key bit', int.bit_length(public.n))
    print('key len', len(str(public.n)))
    encrypted = encryptLargeFile(msg, public)
    with open('encryptedimg', 'w') as outfile:
        outfile.write(str(encrypted))

if decision is 'b':
    private = loadPrivateKey()
    encrypted = open('encryptedimg', 'r').read()
    decryptedVal = decryptLargeFile(encrypted, private)
    
    print('pixels!', decryptedVal)
    pixels = np.asarray(ast.literal_eval(decryptedVal))
    # pixels = decryptedVal.rstrip('\0')[1:-1].split(',')
    print('pixels2', pixels)
    decryptedImage = createImage(pixels)
    decryptedImage.show()



# generate keys
if decision is 'g':
    private, public = generateKeys()
    encodeAndSavePrivate(private)
    encodeAndSavePublic(public)

# encrypt
if decision is 'e':
    public = loadPublicKey()
    image = openImage('images/lena-greyscale-small.png')
    image.show()
    pixels = getPixelArray(image)
    # print(pixels)
    strImg = str(pixels)
    print('pixels', strImg)
    # encryptedImg = encrypt('[12, 123, 1231, 231231231333, 123 ]', public)
    encryptedImg = encrypt(strImg, public)
    print(encryptedImg)

    with open('encryptedimg', 'w') as outfile:
        outfile.write(str(encryptedImg))

# decrypt
if decision is 'd':
    private = loadPrivateKey()
    print('BIT LENGTH OF N', int.bit_length(private.n))
    encryptedImg = open('encryptedimg', 'r').read()
    print(encryptedImg)
    decryptedVal = decrypt(int(encryptedImg), private)
    print('asdasd', decryptedVal)
    originalMsg = asciiToText(decryptedVal)
    print(originalMsg)
    
    # pixels = ast.literal_eval(asciiToText(decryptedStr))
    # decryptedImage = createImage(pixels)
    # decryptedImage.show()
    # print(text)