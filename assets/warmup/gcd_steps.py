from PIL import Image
from math import sqrt, sin
import numpy as np

def gcd_steps(u, v):
    steps = 0
    while v:
        u, v = v, u % v
        steps += 1
    return steps

# http://stackoverflow.com/questions/20792445/calculate-rgb-value-for-a-range-of-values-to-create-heat-map
def rgb(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    ratio = 2 * (value-minimum) / (maximum - minimum)
    r = int(max(0, 255*(1 - ratio)))
    b = int(max(0, 255*(ratio - 1)))
    g = 255 - b - r
    return r, g, b

img = Image.new('RGB', (300,300), 'black')
pixels = img.load()

steps = np.zeros(shape=(img.size[0], img.size[1]))
for i in range(img.size[0]):
    for j in range(img.size[1]):
        steps[i,j] = gcd_steps(i + 1, img.size[1] - j)

m = np.amax(steps)
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i,j] = rgb(0, m, steps[i,j])

img.save('gcd_steps.png')

