import svgwrite
from math import sin,sqrt,tan,cos,pi

def render(lines):
    dwg = svgwrite.Drawing('b_pentagram_abs.svg', profile='tiny')
    stroke = svgwrite.rgb(10, 10, 16, '%')

    minx, miny = 0,0

    for f,t in lines:
        # Reverse
        f = f[0] * -1, f[1] * -1
        t = t[0] * -1, t[1] * -1

        # Note minx and miny
        if f[0] < minx: minx = f[0]
        if t[0] < minx: minx = t[0]
        if f[1] < miny: miny = f[1]
        if t[1] < miny: miny = t[1]

    for f,t in lines:
        # Reverse
        f = f[0] * -1, f[1] * -1
        t = t[0] * -1, t[1] * -1

        f = f[0] - minx, f[1] - miny
        t = t[0] - minx, t[1] - miny

        dwg.add(dwg.line(f, t, stroke=stroke))

    dwg.save()

###
edge = 200

scale = lambda v: tuple(map(lambda x: x*edge, v))

c1 = cos(2/5 * pi)
c2 = cos(pi/5)

s1 = sin(2/5 * pi)
s2 = sin(4/5 * pi)

p = [None for _ in range(5)]

p[0] = (0,1)
p[1] = (s1, c1)
p[2] = (s2, -c2)
p[3] = (-s2, -c2)
p[4] = (-s1, c1)

for i in range(5):
    p[i] = scale(p[i])

lines = []

for i in range(5):
    f, t = p[i], p[(i + 1) % 5]
    lines.append((f,t))

for i in range(5):
    f, t = p[i], p[(i + 2) % 5]
    lines.append((f,t))

render(lines)
