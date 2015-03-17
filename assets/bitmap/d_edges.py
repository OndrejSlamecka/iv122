from PIL import Image

img = Image.open('d_edges_in.png')
pixels = img.load()

for i in range(1, img.size[0] - 1):
    for j in range(1, img.size[1] - 1):
        c = sum(pixels[i,j])
        v = sum(pixels[i,j+1]) # vertical
        h = sum(pixels[i+1,j]) # horizontal
        if abs(c-v) > 3 or abs(c-h) > 3:
            pixels[i,j] = (255,255,255)

img.save('d_edges_out.png')

