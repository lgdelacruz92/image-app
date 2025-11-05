import sys
import os

inputfile = sys.argv[1]
outputfile = sys.argv[2]


# Get the parent directory and add it to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from common import *

def make_rgb(img, pixels, r_npix, y_npix, b_npix):
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            # print(r, g, b)
            r_npix[x,y] = (r, 0, 0)
            y_npix[x,y] = (0, g, 0)
            b_npix[x,y] = (0, 0, b)
            # print(npix[x,y])

if __name__ == '__main__':
    pixels, img = load_image(inputfile)
    r_npix, r_nimg = make_new_image(img)
    y_npix, y_nimg = make_new_image(img)
    b_npix, b_nimg = make_new_image(img)



    make_rgb(img, pixels, r_npix, y_npix, b_npix)

    r_nimg.save(f'red-{outputfile}.jpg')
    y_nimg.save(f'yellow-{outputfile}.jpg')
    b_nimg.save(f'blue-{outputfile}.jpg')