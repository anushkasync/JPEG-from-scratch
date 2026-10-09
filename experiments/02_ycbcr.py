from PIL import Image
import numpy as np

from jpeg.color import rgb_to_ycbcr


image = Image.open("examples/input.png").convert("RGB")
pixels = np.array(image)

y, cb, cr = rgb_to_ycbcr(pixels)

print("Y shape:", y.shape)
print("Cb shape:", cb.shape)
print("Cr shape:", cr.shape)

print("RGB:", pixels[0, 0])
print("Y:", y[0, 0])
print("Cb:", cb[0, 0])
print("Cr:", cr[0, 0])