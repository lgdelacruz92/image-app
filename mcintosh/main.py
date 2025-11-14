import sys
import os
import matplotlib.pyplot as plt

inputfile = sys.argv[1]
outputfile = sys.argv[2]


# Get the parent directory and add it to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from common import *
dark = (40, 40, 40)
light = (160, 160, 160)
highlight= (255, 255, 255)
def make_bw(img, pixels, npix):
    # arr = [0 for i in range(256)]
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            v = int((0.299 * r) + (0.587 * g) + (0.114 * b))
            npix[x,y] = (v, v, v)
            # if v <= 40:
            #     npix[x,y] = dark
            # elif v <= 160:
            #     npix[x,y] = light
            # else:
            #     npix[x, y] = highlight

            # arr[v] += 1
    # make_scatter_plot([i for i in range(256)], arr)

def make_scatter_plot(x, y):

    # Create scatter plot
    plt.scatter(x, y, color='blue', marker='o', s=100) 
    plt.title("Basic Scatter Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)

    # Show the plot
    plt.show()
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