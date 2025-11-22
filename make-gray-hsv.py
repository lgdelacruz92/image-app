from PIL import Image, ImageEnhance
import numpy as np

img = Image.open("leaf/leaf.jpg").convert("HSV")
H, S, V = img.split()

# Convert S to numpy array for editing
S_data = np.array(S)

# Add 40 to saturation
S_data = np.clip(S_data * 0, 0, 255)

# Convert back to Pillow image
S = Image.fromarray(S_data.astype('uint8'), 'L')

# Merge back into HSV
hsv_modified = Image.merge("HSV", (H, S, V))

# Convert to RGB to view/save
rgb_out = hsv_modified.convert("RGB")
rgb_out.show()
