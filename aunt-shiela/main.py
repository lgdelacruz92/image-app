import sys
import os

inputfile = sys.argv[1]
outputfile = sys.argv[2]


# Get the parent directory and add it to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from common import *
dark = (30, 30, 30)
light = (200, 200, 200)
highlight= (255, 255, 255)
def make_bw(img, pixels, npix):
    x_min = 255
    x_max = 0
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            v = int((0.299 * r) + (0.587 * g) + (0.114 * b))
            if 100 < v and v < 115:
                npix[x,y] = dark
            elif v < 155:
                npix[x,y] = light
            elif v < 255:
                npix[x,y] = highlight
            else:
                npix[x,y] = (255, 0, 0)
            # npix[x,y] = (v, v, v)


    # print(x_min, x_max)


def make_dark(img, pixels, npix):
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            v = ( r + g + b ) // 3
            npix[x,y] = (v, v, v)

if __name__ == '__main__':
    pixels, img = load_image(inputfile)
    npix, nimg = make_new_image(img)


    make_bw(img, pixels, npix)

    nimg.save(f'{outputfile}.jpg')