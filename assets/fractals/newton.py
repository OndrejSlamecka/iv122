#!/usr/bin/env python3

# TODO: Maybe implement some smoothing technique? (See http://www.mitchr.me/SS/newton/)

from PIL import Image
from math import floor, sin, cos, log

def f(z): return z**8 + 15*z**4 - 16

def draw(x_side, y_side, pixels, f, x_range, y_range, n_max_iter, h, eps, colour):
    c_zy = lambda y: y * (y_range[1] - y_range[0]) / (y_side - 1) + y_range[0]
    c_zx = lambda x: x * (x_range[1] - x_range[0]) / (x_side - 1) + x_range[0]
    c_z = lambda x,y: complex(c_zy(y), c_zx(x))

    # For each point on the complex plane
    for y in range(y_side):
        for x in range(x_side):
            z = z0 = z1 = c_z(x,y)

            for i in range(n_max_iter):
                # See http://en.wikipedia.org/wiki/Numerical_differentiation
                dz = (f(z + complex(h, h)) - f(z)) / complex(h, h)
                z0 = z - f(z) / dz
                if abs(z0 - z) < eps:
                    break
                z1 = z
                z = z0

            pixels[x, y] = colour(z0, z1, i)

def colour1(z0, z1, n):
    return (n % 8 * 32, n % 8 * 32, n % 8 * 32)

def colour2(z0, z1, n):
    r = floor(((sin(n + abs(z1 - z0)) + 1) / 2) * 255)
    g = floor(((cos(n + abs(z1 - z0)) + 1) / 2) * 255)
    b = r ^ g
    return (r,g,b)

def colour3(z0, z1, n):
    r = floor(((sin(log(n + abs(z1 - z0))) + 1) / 2) * 255)
    g = floor(((cos(log(n + abs(z1 - z0))) + 1) / 2) * 255)
    b = r ^ g
    return (r,g,b)


if __name__ == "__main__":
    side = 840
    x_side = side
    y_side = side

    image = Image.new("RGB", (x_side, y_side))
    pixels = image.load()

    draw(x_side, y_side, pixels, f, [-1,1], [-1,1], 25, 1e-5, 1e-5, colour1)

    image.save("newton.png", "PNG")
