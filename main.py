import ast
import base64
import numpy as np
from image import *
from rsaCrypto import *
from openKeys import *
from generateKeys import *
from keysBase64 import *
from PIL import Image

a = loadPublicKey()
print('len',len(str(a.n)))
print('bytecount', int.bit_length(a.n))

decision = input('Generate, Encrypt or decrypt?')
# generate keys
if decision is 'g':
    private, public = generateKeys()
    encodeAndSavePrivate(private)
    encodeAndSavePublic(public)

# encrypt
if decision is 'e':
    openImage('images/lena-greyscale.png').show()
    with open('images/lena-greyscale.png', "rb") as imageFile:
        image64 = base64.b64encode(imageFile.read()).decode()
        # image64 = image64.decode()

    public = loadPublicKey()
    encrypted = encryptLargeFile(image64, public)

    with open('encryptedimg', 'w') as outfile:
        outfile.write(str(encrypted))

# decrypt
if decision is 'd':
    private = loadPrivateKey()

    encrypted = open('encryptedimg', 'r').read()
    decryptedVal = decryptLargeFile(encrypted, private)
    decryptedBytes = base64.b64decode(decryptedVal)

    # print(decryptedBytes)
    
    with open('images/new.png', 'wb') as outfile:
        outfile.write(decryptedBytes)

    openImage('images/new.png').show()
        
