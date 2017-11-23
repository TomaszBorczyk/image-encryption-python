from PIL import Image
import ast

def openImage(filename):
    return Image.open(filename)

def showImage(image):
    image.show()

def getPixelArray(image):
    return list(image.getdata())



# print(pixels)

# a = [1, 2, 3]
# print(a)
# b = str(a)
# print(b)
# c = ast.literal_eval(b)
# print(c)
# print(c[0])

# image = openImage('lena-greyscale-small.png')
# image.show()
# print(getPixelArray(image))

