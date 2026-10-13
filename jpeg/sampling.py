import numpy as np

def chroma_subsample_420(channel):
    height, width = channel.shape

    if height % 2 != 0 or width % 2 != 0:
        raise ValueError("Image height and width must be even")

    top_left = channel[0::2, 0::2]
    top_right = channel[0::2, 1::2]
    bottom_left = channel[1::2, 0::2]
    bottom_right = channel[1::2, 1::2]

    return (
        top_left + top_right + bottom_left + bottom_right
    ) / 4.0