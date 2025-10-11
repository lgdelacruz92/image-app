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
    "-l", "--low",
    type=int,
    required=True,
    help="min limit for dark"
)

parser.add_argument(
    '-m', '--max',
    type=int,
    required=True,
    help='max limit for dark'
)

args = parser.parse_args()

# Get the parent directory and add it to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from common import *

def make_dark(img, pixels, npix):
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            v = ( r + g + b ) // 3
            if args.low < v and v < args.max:
                npix[x,y] = (args.max, args.max, args.max)
            else:
                npix[x,y] = (255, 255, 255)

if __name__ == '__main__':
    pixels, img = load_image(args.inputfile)
    npix, nimg = make_new_image(img)


    make_dark(img, pixels, npix)

    nimg.save(f'{args.outputfile}.jpg')