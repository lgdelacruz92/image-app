from PIL import Image
import sys, os

path = sys.argv[1]
layer = sys.argv[2]
if layer not in set(['shadow', 'midtones', 'avg', 'highlight']):
    raise ValueError(layer)

shadow_t = 40
midtones_t = 150
highlight_t = 200
shadow = (0, shadow_t)
midtones = (shadow_t, midtones_t)
avg = (midtones_t, highlight_t)
highlight = (highlight_t, 256)

def load_image(path):
    img = Image.open(path)
    img = img.convert("RGB")
    pixels = img.load()
    return (pixels, img)

def make_new_image(img):
    xnew_image = Image.new('RGB', (img.width, img.height))
    new_image_pixels = xnew_image.load()
    return (new_image_pixels, xnew_image)

def get_layer_val(layer):
    if layer == 'shadow':
        return shadow
    elif layer == 'midtones':
        return midtones
    elif layer == 'avg':
        return avg
    elif layer == 'highlight':
        return highlight
    else:
        raise ValueError(layer)

def make_new_layer(path, layer):
    o_pixels, img = load_image(path)
    n_pixels, new_img = make_new_image(img)
    layer_val = get_layer_val(layer)

    for x in range(img.width):
        for y in range(img.height):
            r, g, b = o_pixels[x, y]
            v = (r + g + b) // 3
            if layer_val[0] <= v and v < layer_val[1]:
                color_val = (layer_val[0] + layer_val[1]) // 2
                n_pixels[x, y] = (color_val, color_val, color_val)
            else:
                n_pixels[x, y] = (255, 255, 255)
    new_path = os.path.dirname(path)
    filename = os.path.basename(path)
    new_img.save(os.path.join(new_path, f'{filename.replace('.jpg', '')}-{layer}.jpg'))

make_new_layer(path, layer)