import sys
import os
import argparse

parser = argparse.ArgumentParser(description="Example script with optional argument")
    
# Optional argument (note the `--` prefix)
parser.add_argument(
    "-i", "--inputfile",
    type=str,
    required=True,
    help="input file (with extension)"
)

parser.add_argument(
    "-o", "--outputfile",
    type=str,
    required=True,
    help="output file (no extension)"
)

parser.add_argument(
    "-d", "--dark",
    nargs=2,
    type=int,
    required=True,
    help="dark"
)

parser.add_argument(
    '-m', '--mid',
    nargs=2,
    type=int,
    required=True,
    help='mid'
)

parser.add_argument(
    '-a', '--avg',
    nargs=2,
    type=int,
    required=True,
    help='avg'
)

args = parser.parse_args()

# Get the parent directory and add it to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from common import *

def make_white(img, npix):
    for x in range(img.width):
        for y in range(img.height):
            npix[x,y]=(255, 255, 255)

def make_dark(img, pixels, npix, l, h):
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            v = ( r + g + b ) // 3
            if l < v and v < h:
                npix[x,y] = (h, h, h)

if __name__ == '__main__':
    pixels, img = load_image(args.inputfile)
    npix, nimg = make_new_image(img)


    make_white(img, npix)

    d1, d2 = args.dark
    m1, m2 = args.mid
    a1, a2 = args.avg

    # dark
    make_dark(img, pixels, npix, d1, d2)
    # mid
    make_dark(img, pixels, npix, m1, m2)
    # avg
    make_dark(img, pixels, npix, a1, a2)

    nimg.save(f'{args.outputfile}.jpg')