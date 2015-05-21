from math import sin, cos, pi
import random
import svgwrite

plane_size = 500
lineseg_len = 120

def render(lines, points):
    dwg = svgwrite.Drawing('linreg.svg', profile='tiny')
    stroke = svgwrite.rgb(10,10,16,'%')

    minx = 0
    miny = 0
    for p in points:
        if p[0] < minx:
            minx = p[0]
        if p[1] < miny:
            miny = p[1]

    for f, t in lines:
        dwg.add(dwg.line(f, t, stroke=stroke))

    for p in points:
        dwg.add(dwg.circle((p[0] - minx, p[1] - miny), r = 3))

    dwg.save()

def read_points(filename):
    points = []
    for line in open(filename):
        x,y = line.rstrip().split()
        x,y = float(x), float(y)
        points.append((x*100,y*100))

    return points

lines = []
points = read_points('linreg.txt')
render(lines, points)

