from PIL import Image
import sys
import os

# Get the parent directory and add it to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from common import *

t = 100

if __name__ == '__main__':
    pixels, img = load_image('./turtle1.jpg')
    npix, nimg = make_new_image(img)

    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]

            if b > t and g > t and r > t:
                npix[x,y] = (r, g, b)
            else:
                npix[x,y] = (0, 0, 0)


    nimg.save('all-turtle.jpg')