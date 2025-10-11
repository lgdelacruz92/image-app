from PIL import Image
import sys, os

path = sys.argv[1]

def load_image(path):
    img = Image.open(path)
    img = img.convert("RGB")
    pixels = img.load()
    return (pixels, img)

def make_new_image(img):
    xnew_image = Image.new('RGB', (img.width, img.height))
    new_image_pixels = xnew_image.load()
    return (new_image_pixels, xnew_image)


def make_new_layer(path):
    o_pixels, img = load_image(path)
    n_pixels, new_img = make_new_image(img)

    for x in range(img.width):
        for y in range(img.height):
            r, g, b = o_pixels[x, y]
            v = (r + g + b) // 3
            v = (v // 50) * 50 
            n_pixels[x, y] = (v, v, v)
    new_path = os.path.dirname(path)
    filename = os.path.basename(path)
    new_img.save(os.path.join(new_path, f'{filename.replace('.jpg', '')}-gradient.jpg'))

make_new_layer(path)