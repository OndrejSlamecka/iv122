from PIL import Image
from math import sqrt, sin, cos, pi

side = 400
img = Image.new('RGB', (side,side), 'white')
pixels = img.load()

def rgb(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    ratio = 2 * (value-minimum) / (maximum - minimum)
    r = int(max(0, 255*(1 - ratio)))
    b = int(max(0, 255*(ratio - 1)))
    g = 255 - b - r
    return r, g, b

dist = 0
angle = 0
while dist < side//2:
    x, y = cos(angle * pi/180) * dist, sin(angle * pi/180) * dist
    c = rgb(-20000, 20000, x*y)
    pixels[side//2 + x, side//2 + y] = c
    pixels[side//2 + x+1, side//2 + y] = c
    pixels[side//2 + x, side//2 + y + 1] = c
    angle += 0.05
    dist += 0.004

img.save('a_spiral.png')

