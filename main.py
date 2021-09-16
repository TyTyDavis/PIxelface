from PIL import Image
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

img = Image.open(os.path.join(ROOT_DIR, "Portrait.jpg"))



img.save(os.path.join(ROOT_DIR, "newPortrait.png"))
img.close()
