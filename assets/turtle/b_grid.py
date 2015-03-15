import svgwrite

dwg = svgwrite.Drawing('b_grid.svg', profile='tiny')
stroke = svgwrite.rgb(10, 10, 16, '%')

edge = 200
lines = 21

for i in range(lines):
    l = edge/2 - (edge/lines) * abs(((lines / 2) - i))

    line = dwg.line((edge/10*i, edge/2 - l), (edge/10*i, edge/2 + l), stroke=stroke)
    dwg.add(line)


dwg.save()
