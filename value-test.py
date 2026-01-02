import sys
import os

inputfile = sys.argv[1]
outputfile = sys.argv[2]


# Get the parent directory and add it to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from common import *

def make_bw(img, pixels, npix):
    radius = 10
    x1 = 700
    y1 = 100
    avgV = 0
    count = 0
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            v = int((0.299 * r) + (0.587 * g) + (0.114 * b))

            if x > x1 + radius or x < x1 - radius or y > y1 + radius or y < y1 - radius:
                npix[x,y] = (v, v, v)
            else:
                avgV += v
                count += 1
                npix[x,y] = (255, 0, 0)
    print(avgV // count)
if __name__ == '__main__':
    pixels, img = load_image(inputfile)
    npix, nimg = make_new_image(img)


    make_bw(img, pixels, npix)

    nimg.save(f'{outputfile}.jpg')