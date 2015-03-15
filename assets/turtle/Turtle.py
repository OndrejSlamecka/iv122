import math
import svgwrite

class Turtle:
    def __init__(self, filename):
        self.x = 0
        self.y = 0
        self.angle = math.pi/2
        self.pen = True
        self.lines = []

        self.dwg = svgwrite.Drawing(filename + '.svg', profile='tiny')
        self.stroke = svgwrite.rgb(10, 10, 16, '%')

    def forward(self, dist):
        nx = self.x + math.cos(self.angle) * dist
        ny = self.y + math.sin(self.angle) * dist

        if self.pen:
            self.lines.append((self.x, self.y, nx, ny))

        self.x, self.y = nx, ny

    def back(self, step):
        self.forward(-step)

    def right(self, angle):
        self.angle += angle * math.pi/180

    def left(self, angle):
        self.angle -= angle * math.pi/180

    def pen_up(self):
        self.pen = False

    def pen_down(self):
        self.pen = True

    def save(self):
        min_x, min_y = 0,0

        for (x1, y1, x2, y2) in self.lines:
            min_x = min(min_x, x1)
            min_x = min(min_x, x2)

            min_y = min(min_y, y1)
            min_y = min(min_y, y2)

        min_x, min_y = -min_x, -min_y

        for (x1, y1, x2, y2) in self.lines:
            fr = (min_x + x1, min_y + y1)
            to = (min_x + x2, min_y + y2)
            line = self.dwg.line(fr, to, stroke=self.stroke)
            self.dwg.add(line)

        self.dwg.save()

