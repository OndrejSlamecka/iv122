from PIL import Image

img = Image.open('d_xor_in.png')
pixels = img.load()

for i in range(0, img.size[0]):
    for j in range(0, img.size[1]):
        if i % 2 or j % 2:
            r,g,b,a = pixels[i,j]
            pixels[i,j] = (255-r,255-g,255-b)

img.save('d_xor_out.png')

