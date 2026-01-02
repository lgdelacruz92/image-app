import sys
import os

inputfile = sys.argv[1]
# outputfile = sys.argv[2]


# Get the parent directory and add it to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from common import *

def make_bw(img, pixels, npix, comb):
    for x in range(img.width):
        for y in range(img.height):
            v = pixels[x, y]
            # v = int((0.299 * r) + (0.587 * g) + (0.114 * b))
            # (r,b,g),(g,r,b)(g,b,r)(b,r,g)(b,g,r)
            npix[x,y] = (v[comb[0]], v[comb[1]], v[comb[2]])

if __name__ == '__main__':
    pixels, img = load_image(inputfile)
    npix, nimg = make_new_image(img)
    letters = ['r','g','b']
    for comb in [(0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)]:
        make_bw(img, pixels, npix, comb)
        nimg.save(f'./cow/cow-{letters[comb[0]]}{letters[comb[1]]}{letters[comb[2]]}.jpg')