from PIL import Image
from math import sqrt, sin

def gen_gradient(red_function, image_name):
    img = Image.new('RGB', (255,255), 'black')
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i,j] = (red_function(i), 255 - j, round(sqrt(i*i + j*j)))

    img.save(image_name)

gen_gradient(lambda i: 255 - i, 'colours.png')
gen_gradient(lambda i: round((255 - i) * (1+(i/255)**2)), 'colours_more_red.png')
gen_gradient(lambda i: round((255 - i) * ((1 + i/255)**2)), 'colours_much_more_red.png')

