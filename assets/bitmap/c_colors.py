from PIL import Image
from math import sqrt, sin, cos, pi

side = 800
img = Image.new('RGB', (side,side), 'white')
pixels = img.load()

for x in range(-side//2, side):
    for y in range(-side//2, side//2):
        if sqrt(x*x + y*y) < side//2:
            if x > 0 and y < 0:
                pixels[x + side//2, y + side//2] = (x^127, y & 128 - y^x, x^y)
            else:
                pixels[x + side//2, y + side//2] = (x^127, y | 128 - y^x, x^y)

img = img.resize((side // 2, side // 2), Image.ANTIALIAS)
img.save('c_colors.png')

