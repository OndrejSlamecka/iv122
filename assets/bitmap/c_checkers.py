from PIL import Image
from math import sqrt, sin

side = 400
dd = 400 // 5 # side of four patches

img = Image.new('RGB', (side,side), 'white')
pixels = img.load()

# Generate checkers
for i in range(side):
    for j in range(side):
        c = (255,255,255)
        if    i % dd < dd/2 and j % dd > dd/2 \
           or i % dd > dd/2 and j % dd < dd/2:
            c = (0,0,0)
        
        pixels[i, j] = c

# Invert colors in circles of various radius
for k in [5,3,2]:
    for i in range(-side//2, side//2):
        for j in range(-side//2, side//2):
            if sqrt(i*i + j*j) < side//k:
                x, y = side//2 + i, side//2 + j
                if pixels[x,y] == (0,0,0):
                    pixels[x,y] = (255,255,255)
                else:
                    pixels[x,y] = (0,0,0)

img = img.resize((side // 2, side // 2), Image.ANTIALIAS)
img.save('c_checkers.png')
