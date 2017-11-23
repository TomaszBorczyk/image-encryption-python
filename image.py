from PIL import Image

def openImage(filename):
    return Image.open(filename)

def showImage(image):
    image.show()

def getPixelArray(image):
    return list(image.getdata())