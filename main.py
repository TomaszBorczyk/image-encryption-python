import ast
from image import *
from rsaCrypto import *
from openKeys import *
from generateKeys import *

# # encrypt
# public = getPublic()
# image = openImage('images/lena-greyscale-small.png')
# # image.show()
# pixels = getPixelArray(image)

# strImg = str(pixels)
# encryptedImg = encrypt(strImg, public)

# with open('test', 'w') as outfile:
#     outfile.write(str(encryptedImg))

# decrypt
private = getPrivate()
encryptedImg = open('test', 'r').read()
print(encryptedImg)
decryptedStr = decrypt(int(encryptedImg), private)
print(decryptedStr)
