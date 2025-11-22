import sys
import os

inputfile = sys.argv[1]


# Get the parent directory and add it to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from common import *

def make_bw(w, h, npix):
    for x in range(w):
        for y in range(h):
            npix[x,y] = (x, x, x)

if __name__ == '__main__':
    w = 256
    h = 256
    npix, nimg = make_new_image_wh(w, h)


    make_bw(w, h, npix)

    nimg.save(f'{inputfile}.jpg')