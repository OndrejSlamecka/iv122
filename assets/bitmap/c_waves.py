from PIL import Image
from math import sin, ceil, sqrt

side = 400

img = Image.new('RGB', (side,side), 'white')
pixels = img.load()

for i in range(-side//2, side//2):
    for j in range(-side//2, side//2):
        d = sqrt(i*i + j*j)
        c = ceil(((sin(1/5*d) + 1) * 128))
        pixels[side//2 + i, side//2 + j] = (c,c,c)

for i in range(-side//3, side//3):
    for j in range(-side//3, side//3):
        r,g,b = pixels[side//2 + i, side//2 + j]
        pixels[side//2 + i, side//2 + j] = (255 - r, 255 - g, 255 - b)

img = img.resize((side // 2, side // 2), Image.ANTIALIAS)
img.save('c_waves.png')
