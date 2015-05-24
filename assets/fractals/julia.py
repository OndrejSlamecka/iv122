#!/usr/bin/env python3

from PIL import Image
import colorsys
from math import exp, sin, log

def draw(x_side, y_side, pixels, c, n_terations, i):
    x_range = [-1,1]
    y_range = [-1,1]

    for x in range(x_side):
        xre = x_range[0] + (x_range[1] - x_range[0]) * x / x_side
        for y in range(y_side):
            z = complex(xre, y_range[0] + (y_range[1] - y_range[0]) * y / y_side)

            smooth = exp(-abs(z))
            for i in range(256):
                z = z * z + c
                smooth += exp(-abs(z))
                if abs(z) > 2.0:
                    break

            v = 0.6+0.4*(sin(smooth / 10))
            r = int(v * 256)
            g = int(v * v**(1 + i / (n_iterations / 2)) * 256)
            b = int(v * v**(2 + i / (n_iterations / 2)) * 256)

            pixels[x, y] = (r,g,b)

if __name__ == "__main__":
    n_iterations = 1000
    for i in range(n_iterations): # iterate from 0.1 to 0.8
        x_side = y_side = 1080
        image = Image.new("RGB", (x_side, y_side))
        pixels = image.load()

        c = complex(0.30 + i / (n_iterations * 7), 0.30 + i / (n_iterations * 7))
        draw(x_side, y_side, pixels, c, n_iterations, i)

        image.save('julia_anim/' + str(i) + '.png', 'PNG')
        print(str(i) + ' done.')

