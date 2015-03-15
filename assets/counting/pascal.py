import math
import svgwrite

# http://stackoverflow.com/questions/20792445/calculate-rgb-value-for-a-range-of-values-to-create-heat-map
def rgb(minimum, maximum, value):
        minimum, maximum = float(minimum), float(maximum)
        ratio = 2 * (value-minimum) / (maximum - minimum)
        r = int(max(0, 255*(1 - ratio)))
        b = int(max(0, 255*(ratio - 1)))
        g = 255 - b - r
        return r, g, b

class BlockPainter:
    def __init__(self, filename):
        self.block_size = 8
        self.dwg = svgwrite.Drawing(filename, profile='tiny')

    def draw_block(self, coords, color):
        x = coords[0]*self.block_size + (coords[1] - 1) * self.block_size // 2
        y = coords[1]*self.block_size
        rect = self.dwg.rect(insert = (x,y),
                size = (self.block_size, self.block_size),
                fill = 'rgb' + str(color))
        self.dwg.add(rect)

    def save(self):
        self.dwg.save()

def draw_pascal(n, d):
    line = [0] * (n+1)
    new_line = [0] * (n+1)

    line[1] = 1

    for i in range(0,n):
        new_line[1] = 1

        for j in range(1,i+2):
            new_line[j] = line[j-1] + line[j]
            bp.draw_block((n//2 - i + j - 1, i), rgb(0, d-1, new_line[j] % d))

        line = list(new_line)

bp = BlockPainter('pascal.svg')
draw_pascal(100, 30)
bp.save()
