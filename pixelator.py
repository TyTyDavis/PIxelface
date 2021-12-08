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
img = Image.open(os.path.join(ROOT_DIR, "Portrait2.png"))
#img = img.rotate(-90, expand=True)
#Change image size
img = resize.pixelResize(img, 150, 200)
colors, pixelCount = extcolors.extract_from_image(img,  tolerance=30,limit=10)

img.save(os.path.join(ROOT_DIR, "Portrait2Small.png"))

#Change color palette
colors = colorPalette.returnRGB(colors)
#add pujre white to palette
colors.append((255,255,255))
newPixels = []
for color in img.getdata():
    colorChoice = colorPalette.nearestColour(colors, color)
    newPixels.append(colorChoice)

newImg = Image.new(img.mode,img.size)
newImg.putdata(newPixels)



newImg.show()
img.close()
