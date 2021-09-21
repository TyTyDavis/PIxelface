import math
import matplotlib
import numpy
import extcolors
import resize
import colorPalette

import PIL
from PIL import Image
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

#instantiate image object
img = Image.open(os.path.join(ROOT_DIR, "Portrait.jpg"))
img = img.rotate(-90, expand=True)
#Change image size
img = resize.pixelResize(img, 100, 200)
colors, pixelCount = extcolors.extract_from_image(img)

img.save(os.path.join(ROOT_DIR, "Portrait.png"))

#Change color pallete
colors = colorPalette.returnRGB(colors)

newPixels = []
for color in img.getdata():
    newPixels.append(colors[0])

newImg = Image.new(img.mode,img.size)
newImg.putdata(newPixels)



newImg.show()
img.close()
