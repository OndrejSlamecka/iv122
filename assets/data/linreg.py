#!/usr/bin/env python3

"""
How to derive the equation:
https://www.youtube.com/watch?v=mIx2Oj5y9Q8
"""

import svgwrite

size_coef = 50 # scale the image up

### I/O
def render(line, points):
    dwg = svgwrite.Drawing('linreg.svg', profile='tiny')
    stroke = svgwrite.rgb(250,10,16,'%')

    minx = 0
    miny = 0
    for p in points:
        if p[0] < minx:
            minx = p[0]
        if p[1] < miny:
            miny = p[1]

    # Draw the line
    f,t = line
    f_x, f_y = f
    t_x, t_y = t
    dwg.add(dwg.line((f_x - minx, f_y - miny), (t_x - minx, t_y - miny), stroke=stroke))

    for p in points:
        dwg.add(dwg.circle((p[0] - minx, p[1] - miny), r = 3))

    dwg.save()

def read_points(filename):
    points = []
    for line in open(filename):
        x,y = line.rstrip().split()
        x,y = float(x), float(y)
        points.append((x*size_coef,y*size_coef))

    return points

### Computations

def linreg(xs, ys):
    # compute m and b in the equation of our line y = m*x + b
    def mean(xs): return sum(xs) / len(xs)

    mean_xy = mean([x*y for (x,y) in zip(xs, ys)])
    mean_xs_squared = mean([x**2 for x in xs])

    m = (mean(xs) * mean(ys) - mean_xy) / (mean(xs)**2 - mean_xs_squared)
    b = mean(ys) - m * mean(xs)

    y = lambda x: m*x + b

    return y

def equation_to_edge(xs, ys, y):
    # compute two points on the line
    minx = min(xs)
    maxx = max(xs)
    edge = ((minx, y(minx)), (maxx, y(maxx)))
    return edge


### Main
if __name__ == "__main__":
    points = read_points('linreg.txt')
    xs = [x for (x,y) in points]
    ys = [y for (x,y) in points]

    y = linreg(xs, ys)
    line = equation_to_edge(xs, ys, y)

    render(line, points)

