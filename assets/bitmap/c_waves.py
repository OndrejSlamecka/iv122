from PIL import Image
from math import sqrt, sin

side = 400

img = Image.new('RGB', (side,side), 'white')
pixels = img.load()

for i in range(side):
    for j in range(side):
        pass # need for sleep...

img = img.resize((side // 2, side // 2), Image.ANTIALIAS)
img.save('c_waves.png')
