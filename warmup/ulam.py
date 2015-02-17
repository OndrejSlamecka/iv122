# Renders Ulam spiral to ulam.bmp
side_length = 500

from PIL import Image
import numpy
import math

def is_prime(n):
    if n == 1 or (n % 2 == 0 and n > 2):
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

# Init image
img = Image.new("RGB", (side_length + 1, side_length + 1), "white")
pixels = img.load()

## Generating the image
x = 0 # x offset from the middle
y = 0

direction = 0 # 0      1      2       3
#		      right    up     left    down
directions = [(1,0), (0,-1), (-1,0), (0,1)]

direction_steps = 1 # number of steps done in a given direction

i = 0
while i < side_length*side_length:
	for j in range(0,2):
		for k in range(0, direction_steps):
			i += 1

			if is_prime(i):
				pixels[side_length//2+x,side_length//2+y] = (0,0,0)
			
			inc = directions[direction]
			x += inc[0]
			y += inc[1]	

		direction = (direction + 1) % 4

	direction_steps += 1
		
img.save('ulam.bmp')

