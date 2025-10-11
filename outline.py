from PIL import Image
import sys

# Load the JPG image
name = sys.argv[1]
img = Image.open(name)

# Convert to RGB (just in case it's not already)
img = img.convert("RGB")
# Create a drawing context


# Access pixels
pixels = img.load()

# new image created
new_image = Image.new('RGB', (img.width, img.height))
new_image_pixels = new_image.load()


# cache = set()

dark_limit = 50

def get_outline(name):
    # Example: invert the colors
    for x in range(img.width):
        for y in range(img.height):
            if x-1 < 0 or x + 1 >= img.width:
                continue
            if y-1 < 0 or y + 1 >= img.height:
                continue
            r, g, b = pixels[x, y]
            v = (r + g + b) // 3
            if v <= dark_limit:
                r1, g1, b1 = pixels[x-1, y]
                v1 = (r1 + g1 + b1) // 3

                r2, g2, b2 = pixels[x, y-1]
                v2 = (r2 + g2 + b2) // 3

                r3, g3, b3 = pixels[x+1, y]
                v3 = (r3 + g3 + b3) // 3

                r4, g4, b4 = pixels[x, y+1]
                v4 = (r4 + g4 + b4) // 3

                if v1 > dark_limit or v2 > dark_limit or v3 > dark_limit or v4 > dark_limit:
                    new_image_pixels[x, y] = (0, 0, 0)
                else:
                    new_image_pixels[x, y] = (255, 255, 255)
            else:
                new_image_pixels[x, y] = (255, 255, 255)

    # print(list(cache))
    new_image.save(name)

get_outline(f'./output/{name.replace('.jpg', '')}-out.jpg')