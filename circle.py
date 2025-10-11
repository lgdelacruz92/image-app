from PIL import Image
import math
# new image created
new_image = Image.new('RGB', (200, 200))
new_image_pixels = new_image.load()

r = 50
cx, cy = (100, 100)
for x in range(new_image.width):
    for y in range(new_image.height):
        if r >= int(math.sqrt((x-cx) ** 2 + (y-cy) ** 2)):
            new_image_pixels[x,y] = (0, 0, 0)
        else:
            new_image_pixels[x,y] = (255, 255, 255)

new_image.save('circle.jpg')