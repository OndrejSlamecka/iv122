from PIL import Image
import numpy
import math

def is_prime(n):
    if n == 1 or (n % 2 == 0 and n > 2):
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

side_length = 500 # Length of side of the resulting image
def spiral_image(is_on_spiral_cb, image_name):
    img = Image.new('RGB', (side_length + 1, side_length + 1), 'white')
    pixels = img.load()

    x = 0 # x offset from the middle
    y = 0

    #             right    up     left    down
    directions = [(1,0), (0,-1), (-1,0), (0,1)]
    direction = 0 # 0       1      2       3

    direction_steps = 1 # number of steps done in a given direction

    i = 0
    while i < side_length*side_length:
        for j in range(0,2):
            for k in range(0, direction_steps):
                i += 1

                if is_on_spiral_cb(i):
                    pixels[side_length//2+x,side_length//2+y] = (0,0,0)

                inc = directions[direction]
                x += inc[0]
                y += inc[1]

            direction = (direction + 1) % 4

        direction_steps += 1

    img.save(image_name)

spiral_image(is_prime, 'ulam_primes.bmp')
spiral_image(lambda x: x % 4 == 0, 'ulam_m4.bmp')
spiral_image(lambda x: x % 5 == 0, 'ulam_m5.bmp')
spiral_image(lambda x: x % 8 == 0, 'ulam_m8.bmp')
