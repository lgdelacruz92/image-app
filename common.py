from PIL import Image

def load_image(path):
    img = Image.open(path)
    img = img.convert("RGB")
    pixels = img.load()
    return (pixels, img)

def make_new_image(img):
    xnew_image = Image.new('RGB', (img.width, img.height))
    new_image_pixels = xnew_image.load()
    return (new_image_pixels, xnew_image)

def make_new_image_wh(w, h):
    xnew_image = Image.new('RGB', (w, h))
    new_image_pixels = xnew_image.load()
    return (new_image_pixels, xnew_image)
