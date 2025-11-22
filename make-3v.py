import sys
import os

inputfile = sys.argv[1]
outputfile = sys.argv[2]


# Get the parent directory and add it to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from common import *

def make_bw(img, pixels, npix):
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            v = int((0.299 * r) + (0.587 * g) + (0.114 * b))
            npix[x,y] = (v, v, v)

if __name__ == '__main__':
    pixels, img = load_image(inputfile)
    npix, nimg = make_new_image(img)


    make_bw(img, pixels, npix)

    nimg.save(f'{outputfile}.jpg')