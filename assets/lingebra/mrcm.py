from math import sin, cos, pi
import svgwrite

def render(lines, points):
    dwg = svgwrite.Drawing('first.svg', profile='tiny')
    stroke = svgwrite.rgb(10,10,16,'%')
    for f, t in lines:
        dwg.add(dwg.line(f, t, stroke=stroke))

    for p in points:
        dwg.add(dwg.circle(p, r = 3))

    dwg.save()


