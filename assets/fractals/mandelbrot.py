#!/usr/bin/env python3

from PIL import Image
from math import log, exp, sin
from colorsys import hls_to_rgb

def draw(x_side, y_side, pixels, x_range, y_range, n_max_iter, colour):
    for y in range(y_side):
        for x in range(x_side):
            c = complex(x_range[0] + (x_range[1] - x_range[0]) * x / x_side,
                        y_range[0] + (y_range[1] - y_range[0]) * y / y_side)
            z = complex(0,0)
            smoothness = exp(-abs(z))

            for i in range(n_max_iter):
                z1 = z
                z = z * z + c
                smoothness += exp(-abs(z))
                if abs(z) >= 3:
                    break

            pixels[x,y] = colour(smoothness, z1, z, i)

def colour1(smoothness, z1, z, i):
    return (i % 4 * 64, i % 8 * 32, i % 16 * 16)

def colour2(smoothness, z1, z, i):
    r = i % 4 * 64
    g = i % 8 * 32
    b = i % 16 * 16

    k = (1 + log(abs(z - z1 + 0.01)))
    r,g,b = int(r * k), int(g * k), int(b * k)
    return (r,g,b)

def colour3(smoothness, z1, z, i):
    r,g,b = hls_to_rgb(30 * smoothness / 256, 1-smoothness/18, 1)
    r,g,b = tuple(map(lambda x: int(x*256), (r,g,b)))
    return (r,g,b)

if __name__ == "__main__":
    y_side = 630
    x_side = 840
    x_range = (-2  , 1)
    y_range = (-1.5, 1.5)

    image = Image.new("RGB", (x_side, y_side))
    pixels = image.load()

    draw(x_side, y_side, pixels, x_range, y_range, 18, colour3)

    image.save("mandelbrot.png", "PNG")
