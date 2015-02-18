"""
 Supersampling is used to antialias the picture
"""

from PIL import Image, ImageDraw
# resulting size is size/ratio
size = 1600
ratio = 4

def shift(coords):
	return (coords[0] + size//2, coords[1] + size//2)

img = Image.new('RGB', (size, size), "white")
draw = ImageDraw.Draw(img)

for i in range(0,11):
	start = (-800 + i*80, 0)
	end = (0, -i*80)

	for j in [(1,1),(-1,1),(1,-1),(-1,-1)]:
		s = (start[0] * j[0], start[1] * j[1])
		e = (end[0]   * j[0], end[1]   * j[1])
		draw.line([shift(s), shift(e)], (0, 0, 0), 6)

img = img.resize((size // ratio, size // ratio), Image.ANTIALIAS)
img.save('cool_pic.png', 'PNG')
