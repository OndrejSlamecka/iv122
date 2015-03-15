import svgwrite
from math import sin,sqrt,tan,cos,pi

dwg = svgwrite.Drawing('b_triangles.svg', profile='tiny')
stroke = svgwrite.rgb(10, 10, 16, '%')

edge = 200
d = 200
x = 0
z = 0
y = sqrt(d**2 - (d/2)**2)

for i in range(9):
    x = x + 10
    d -= 10
    y -= 10 * tan(30 * pi/180)
    z += 10 / cos(30 * pi/180)
    dwg.add(dwg.line((x,y), (edge/2, z), stroke=stroke))
    dwg.add(dwg.line((edge/2, z), (d, y), stroke=stroke))
    dwg.add(dwg.line((x,y), (d, y), stroke=stroke))

dwg.save()
