import math
import matplotlib
import numpy
import extcolors
import resize

import PIL
from PIL import Image
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

#instantiate image object
img = Image.open(os.path.join(ROOT_DIR, "Portrait.jpg"))
img = img.rotate(-90, expand=True)
#Change image size
img = resize.pixelResize(img, 100, 200)

#Change color pallete

img.save(os.path.join(ROOT_DIR, "newPortrait.png"))

#img.show()
img.close()
