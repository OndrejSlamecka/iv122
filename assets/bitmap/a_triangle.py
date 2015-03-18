from PIL import Image
from math import sqrt, floor, ceil

width = 800
height = round(sqrt(3)/2 * width)
img = Image.new('RGB', (width, height), 'white')
pixels = img.load()

def ec(x,y):
    return round(sqrt(x*x + y*y) / width * 255)

def color(x,y):
    r = ec(x + width //2, y)
    g = ec(x, y)
    b = ec(x, y - height / 2)

    return (r, g, b)

for x in range(-width//2, width//2):
    # height from middle is sqrt(3) * width / 2,
    # instead of middle we now have arbitrary point x
    # on the bases of equil. triangles (we can only see
    # halves of these triangles in the upper left and
    # upper right cornes -- the white space)
    y0 = floor(abs(sqrt(3) * x))
    for y in range(y0, height):
        pixels[width // 2 + x, y] = color(x, height - y)

img = img.resize((width // 2, height // 2), Image.ANTIALIAS)
img.save('a_triangle.png')

