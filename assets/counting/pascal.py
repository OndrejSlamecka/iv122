import math
import svgwrite

dwg = svgwrite.Drawing('pascal.svg', profile='tiny')

r = dwg.rect(insert=(1,1), size=(2,2), fill='blue')

dwg.add(r)

dwg.save()
