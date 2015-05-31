#!/usr/bin/env python3

from PIL import Image
from math import log, exp, sin
from colorsys import hls_to_rgb

ratio = 8  # supersampling ratio
offset = 4

def draw_pixel(y_side, pixels, i, x, colour):
    for nx in range(-offset,offset):
        for ny in range(-offset,offset):
            xi, yi = map(sum, zip((i, (x*(y_side-offset - ratio/2)) + offset), (nx,ny)))
            pixels[xi, yi] = colour

def draw(x_side, y_side, x_range, n_iterations, colour):
    for i in range(offset, x_side - offset, offset):
        r = x_range[0] + (x_range[1] - x_range[0]) * i / (x_side - 1)
        x = 0.5
        for j in range(n_iterations):
            x = r * x * (1 - x)
            if j > n_iterations / 2:
                c = colour(j, n_iterations)
                draw_pixel(y_side, pixels, i, x, c)


def colour(j, n_iterations):
    r,g,b = hls_to_rgb(j / n_iterations * 360,0.6,1)
    r,g,b = tuple(map(lambda x: int(x * 256), (r,g,b)))
    return r,g,b

if __name__ == "__main__":
    y_side = 420 * ratio + offset
    x_side = 840 * ratio
    x_range = (-2  , 1)
    y_range = (-1.5, 1.5)

    image = Image.new("RGB", (x_side, y_side))
    pixels = image.load()

    draw(x_side, y_side, [2.9,4], 1000, colour)

    image = image.resize((x_side // ratio, y_side // ratio), Image.ANTIALIAS)
    image.save("bifurcation.png", "PNG")

