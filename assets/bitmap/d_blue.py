from PIL import Image

img = Image.open('d_blue_in.png')
pixels = img.load()

for i in range(0,img.size[0]):
    for j in range(0,img.size[1]):
        r,g,b,a = pixels[i,j]
        if b == 0:
            pixels[i,j] = (0,0,0)

img.save('d_blue_out.png')

