from PIL import Image
import os, sys


# Filter to include only files
n = len(sys.argv[1:])
files = sys.argv[1:n]
print(files)

# new image created

n_image_set = False
new_image = None
color = (0, 0, 0)

for i in range(len(files)):
    f = files[i]
    img = Image.open(f)
    # Convert to RGB (just in case it's not already)
    img = img.convert("RGB")
    # Access pixels
    pixels = img.load()
    if i == 1:
        color = (103, 138, 106)
    elif i == 0:
        color = (78, 66, 94)
    elif i == 2:
        color = (212, 189, 78)
    if not n_image_set:
        new_image = Image.new('RGB', (img.width, img.height), 'white')
        new_image_pixels = new_image.load()
        n_image_set = True
    
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            v = (r + g + b) // 3

            if v <= 210:
                new_image_pixels[x, y] = color
name = sys.argv[n]
new_image.save(f'output/{name}.jpg')