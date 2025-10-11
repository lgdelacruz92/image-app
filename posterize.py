from PIL import Image

# Load the JPG image
img = Image.open("us.jpg")

# Convert to RGB (just in case it's not already)
img = img.convert("RGB")

# Access pixels
pixels = img.load()
new_image = Image.new('RGB', (img.width, img.height), 'white')
new_image_pixels = new_image.load()

d1 = (40, 40, 40)
d2 = (70, 90, 90)
d3 = (96, 112, 112)
midtones = (179, 184, 158)
avg = (205, 209, 190)
highlight = (255, 255, 255)

def color_layer(mininum, maximum, color, name):
    # Example: invert the colors
    i_image = Image.new('RGB', (img.width, img.height), 'white')
    i_image_pixels = i_image.load()
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            v = (r + g + b) // 3
            if mininum <= v and v < maximum:
                new_image_pixels[x, y] = color
                i_image_pixels[x,y] = color
    i_image.save(name)
    




color_layer(0, 100, d3, 'output/d3.jpg')
# color_layer(100, 130, midtones, 'output/midtones.jpg')
# color_layer(130, 210, avg, 'output/avg.jpg')
# color_layer(210, 256, highlight, 'output/highlight.jpg')

new_image.save('output/combined.jpg')