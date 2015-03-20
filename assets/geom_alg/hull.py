from math import sin, cos, pi
import random
import svgwrite

plane_size = 500

def render(lines, points):
    dwg = svgwrite.Drawing('hull.svg', profile='tiny')
    stroke = svgwrite.rgb(10,10,16,'%')

    for f, t in lines:
        dwg.add(dwg.line(f, t, stroke=stroke))

    for p in points:
        dwg.add(dwg.circle(p, r = 3))
    
    dwg.save()

def rand_point():
    x = random.normalvariate(plane_size / 2, plane_size / 4)
    y = random.normalvariate(plane_size / 2, plane_size / 4)
    return round(x), round(y)

# Graham scan, http://en.wikipedia.org/wiki/Graham_scan

def orientation(p1, p2, p3):
    # >0    if p1, p2, p3 are cw
    # <0    if ccw
    #  0    if colinear
    return (p2[0] - p1[0])*(p3[1] - p1[1]) - (p2[1] - p1[1])*(p3[0] - p1[0])

def hull(points):
    """
    i = points.index(min(points, key = lambda p: p[1]))
    points[1], points[i] = points[i], points[1]
    points.sort(key = lambda p: p[1])

    points[0] = points[len(points) - 1]

    m = 1
    for i in range(2, len(points)):
        while orientation(points[m-1], points[m], points[i]) <= 0:
            if m > 1:
                m -= 1
            elif i == len(points):
                break
            else:
                i += 1

        m += 1
        points[m], points[i] = points[i], points[m]

    return points[:m+1]
    """
    
    U, L = [],[]
    points.sort()
    for p in points:
        while len(U) > 1 and orientation(U[-2], U[-1], p) <= 0:
            U.pop()
        while len(L) > 1 and orientation(L[-2], L[-1], p) >= 0:
            L.pop()
        U.append(p)
        L.append(p)
    return U+L

points = [rand_point() for _ in range(40)]

h = hull(points)
lines = []
for i in range(len(h) - 1):
    lines.append((h[i], h[i+1]))

render(lines, points)

