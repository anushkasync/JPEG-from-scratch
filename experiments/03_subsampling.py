import numpy as np
from PIL import Image

from jpeg.color import rgb_to_ycbcr
from jpeg.sampling import chroma_subsample_420

image = Image.open("examples/input.png").convert("RGB")
rgb = np.array(image)

y, cb, cr = rgb_to_ycbcr(rgb)

cb_small = chroma_subsample_420(cb)
cr_small = chroma_subsample_420(cr)

print("Y:", y.shape)
print("Cb before:", cb.shape)
print("Cb after:", cb_small.shape)
print("Cr before:", cr.shape)
print("Cr after:", cr_small.shape)