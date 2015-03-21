from math import sin, cos, pi
import random
import svgwrite

plane_size = 500
lineseg_len = 120

def render(lines, points):
    dwg = svgwrite.Drawing('intersections.svg', profile='tiny')
    stroke = svgwrite.rgb(10,10,16,'%')
    for f, t in lines:
        dwg.add(dwg.line(f, t, stroke=stroke))

    for p in points:
        dwg.add(dwg.circle(p, r = 3))

    dwg.save()


def rand_lineseg():
    #
    #  x,y
    #  |\ <- angle
    #  | \
    # a|  \ lineseg_len
    #  |   \
    #  |    \
    #  ------
    #     b

    x = random.randint(0 + lineseg_len, plane_size - lineseg_len)
    y = random.randint(0 + lineseg_len, plane_size - lineseg_len)

    angle = random.randint(0,360)
    a = cos(angle * 180/pi) * lineseg_len
    b = sin(angle * 180/pi) * lineseg_len

    return ((x,y),(x + b, y + a))

def intersection(l1, l2):
    ((x1, y1), (x2, y2)) = l1
    ((x3, y3), (x4, y4)) = l2

    den = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)

    if den == 0:
        return None

    x = ( (x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4) ) / den
    y = ( (x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4) ) / den

    if   (x < min(x1, x2) or x > max(x1, x2)) or (y < min(y1, y2) or y > max(y1, y2))\
      or (x < min(x3, x4) or x > max(x3, x4)) or (y < min(y3, y4) or y > max(y3, y4)):
        return None

    return x,y

def intersections(lines):
    result = []
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            p = intersection(lines[i], lines[j])
            if p is not None:
                result.append(p)

    return result

lines = [rand_lineseg() for _ in range(40)]

points = intersections(lines)
render(lines, points)

