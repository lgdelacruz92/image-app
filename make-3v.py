import sys
import os

inputfile = sys.argv[1]
outputfile = sys.argv[2]


# Get the parent directory and add it to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from common import *

l = 35
h = 180
def make_bw(img, pixels, npix):
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            v = int((0.299 * r) + (0.587 * g) + (0.114 * b))

            if l < v and v < h:
                if v < 45:
                    npix[x,y] = (0, 0, 255)
                elif v < 140:
                    npix[x,y] = (255, 0, 0)
                else:
                    npix[x,y] = (0, 255, 0)
            else:
                npix[x,y] = (255, 255, 255)

if __name__ == '__main__':
    pixels, img = load_image(inputfile)
    npix, nimg = make_new_image(img)


    make_bw(img, pixels, npix)

    nimg.save(f'{outputfile}.jpg')