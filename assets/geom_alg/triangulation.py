from math import sqrt
import random
import svgwrite

plane_size = 500

def rand_point():
    x = random.randint(0, plane_size)
    y = random.randint(0, plane_size)
    return x,y

def render(lines, points):
    dwg = svgwrite.Drawing('triangulation.svg', profile='tiny')
    stroke = svgwrite.rgb(10,10,16,'%')
    for f, t in lines:
        dwg.add(dwg.line(f, t, stroke=stroke))

    for p in points:
        dwg.add(dwg.circle(p, r = 3))

    dwg.save()

def intersection(l1, l2):
    ((x1, y1), (x2, y2)) = l1
    ((x3, y3), (x4, y4)) = l2

    den = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)

    if den == 0:
        return None

    if    x1 == x3 and y1 == y3 \
       or x2 == x3 and y2 == y3 \
       or x1 == x4 and y1 == y4 \
       or x2 == x4 and y2 == y4:
        return None

    x = ( (x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4) ) / den
    y = ( (x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4) ) / den

    if   (x < min(x1, x2) or x > max(x1, x2)) or (y < min(y1, y2) or y > max(y1, y2))\
      or (x < min(x3, x4) or x > max(x3, x4)) or (y < min(y3, y4) or y > max(y3, y4)):
        return None

    return x,y


def intersection_lines(l1, lines):
    for l2 in lines:
        if intersection(l1, l2) is not None:
            return True

    return False

def line_length(l):
    (x1, y1), (x2, y2) = l
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def triangulate(points):
    potential_lines = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            potential_lines.append((points[i], points[j]))

    potential_lines.sort(key=line_length)

    lines = []
    for l1 in potential_lines:
        if not intersection_lines(l1, lines):
            lines.append(l1)

    return lines

points = [rand_point() for _ in range(200)]
lines = triangulate(points)
render(lines, points)

