#!/usr/bin/env python3

from PIL import Image
from random import randint
from math import sqrt, sin, cos, pi

def draw(pixels, side, points, r, n_steps):
    p = (side//2, side//2)
    for i in range(n_steps):
        a = points[randint(0,len(points)-1)]  # Select point at random
        d = (a[0] - p[0], a[1] - p[1])  # Vector A-P
        dr = map(lambda x: x*r, d)  # Stretch the vector by r
        p = map(sum, zip(p, dr))  # Move our point to p+dr
        pixels[p[0], p[1]] = (0,0,0)

def pil_draw(side, name, cb):
    img = Image.new('RGB', (side, side), (255,255,255))
    pixels = img.load()
    cb(pixels)
    img.save(name + '.png')

def sierpinsky(side):
    triangle = [(0, side), (side / 2, 0), (side, side)]
    pil_draw(side, 'sierpinsky', lambda pixels: draw(pixels, side, triangle, 0.5, 1000000))

def n_gon(side, n, r, n_steps):
    points = []
    a = 270
    for i in range(n):
        x = side/2 + (cos(a * pi / 180) * side/2)
        y = side/2 + (sin(a * pi / 180) * side/2)
        points.append((x, y))
        a += 360 / n

    pil_draw(side, str(n) + 'gon', lambda pixels: draw(pixels, side, points, r, n_steps))

if __name__ == "__main__":
    #sierpinsky(500)
    n_gon(500, 12, 2/3.0, 1000*250)
