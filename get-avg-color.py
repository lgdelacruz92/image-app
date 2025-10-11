import sys, os
from PIL import Image

filepath = sys.argv[1]
basename = os.path.basename(filepath).replace('.jpg', '')
folderpath = os.path.dirname(filepath)


def load_image(path):
    # Load the JPG image
    img = Image.open(path)
    # Convert to RGB (just in case it's not already)
    img = img.convert("RGB")
    # Access pixels
    pixels = img.load()
    
    return (pixels, img)


opixels, img = load_image(filepath)

for x in range(img.width):
    for y in range(img.height):
        r, g, b = opixels[x, y]
        print(( r + g + b) // 3)
        