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
            v = ( r + g + b ) // 3
            if v < 50:
                npix[x,y] = (v, v, v)
            else:
                npix[x,y] = (255, 255, 255)

if __name__ == '__main__':
    pixels, img = load_image(inputfile)
    npix, nimg = make_new_image(img)


    make_bw(img, pixels, npix)

    nimg.save(f'{outputfile}.jpg')