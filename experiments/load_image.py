from PIL import Image
import numpy as np

image = Image.open("examples/input.png").convert("RGB")
pixels = np.array(image)

print("Image size:", image.size)
print("Array shape:", pixels.shape)
print("Data type:", pixels.dtype)
print("First pixel:", pixels[0, 0])