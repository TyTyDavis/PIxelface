import PIL
from PIL import Image

def pixelResize(image, smallHeight, outputHeight):
    initWidth, initHeight = image.size
    ratio = initWidth / initHeight

    height = smallHeight
    width = int(ratio * height)

    image = image.resize((width, height),resample=PIL.Image.BILINEAR, reducing_gap=None)


    height = outputHeight
    width = int(ratio * height)
    image = image.resize((width,height),resample=PIL.Image.NEAREST, reducing_gap=None)

    return image
