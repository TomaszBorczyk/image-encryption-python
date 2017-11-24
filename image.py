import io
from PIL import Image


def openImage(filename):
    return Image.open(filename)

def showImage(image):
    image.show()

def getPixelArray(image):
    return list(image.getdata())

def createImage(pixels):
    return Image.fromarray(pixels)

def getBytes(image):
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, format='PNG')
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr