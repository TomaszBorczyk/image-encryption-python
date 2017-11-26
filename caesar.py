from random import randint, shuffle
from ast import literal_eval
from PIL import Image

def generateCipherReference():
    cipherList = list(range(0, 256))
    shuffle(cipherList)
    IMAGE_TO_CIPHER = list(zip(list(range(0, 256)), cipherList))
    return IMAGE_TO_CIPHER

def reverseCipherReference(reference):
    reversed = list(map(lambda t: (t[1], t[0]), reference))
    reversed.sort(key=lambda tup: tup[0])
    return reversed

def saveToFile(reference):
    with open('caesarCodes/reference.txt', 'w') as outfile:
        outfile.write(reference)

def openCaesarRef():
    with open('caesarCodes/reference.txt', 'r') as outfile:
        caesar = outfile.read()
    return literal_eval(caesar)

def caesarCreate():
    caesar = generateCipherReference()
    saveToFile(str(caesar))

def cipher(cipherMode, inputImagePath, outputImagePath):
    reference = openCaesarRef()
    if cipherMode is 'decrypt':
        reference = reverseCipherReference(reference)

    im = Image.open(inputImagePath)
    print(list(im.getdata()))
    pixelMap = im.load()
    img = Image.new( im.mode, im.size)
    pixelsNew = img.load()
    pixelType = type(pixelMap[0, 0])

    if pixelType is tuple:
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                relevant = (list(pixelMap[i,j])[:3])
                pixelsNew[i,j] = tuple(reference[val][1] for val in relevant)
    
    if pixelType is int:
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                pixelsNew[i,j] = reference[pixelMap[i,j]][1]

    img.show()
    img.save(outputImagePath)
