from PIL import Image
from math import sqrt, sin

side = 400

def gen(path, predicate):
    img = Image.new('RGB', (side,side), 'white')
    pixels = img.load()

    for i in range(-side//2, side//2):
        for j in range(-side//2, side//2):
            x, y = i + side // 2, j + side // 2
            if predicate(i, j):
                pixels[x,y] = (0,0,0)

    img = img.resize((side // 2, side // 2), Image.ANTIALIAS)
    img.save(path)

def disc_pred(x, y):
    return sqrt(x*x + y*y) < side//2

def circle_pred(x, y):
    return side//2 - 2 <= sqrt(x*x + y*y) and sqrt(x*x + y*y) < side//2

gen('a_disc.png', disc_pred)
gen('a_circle.png', circle_pred)

