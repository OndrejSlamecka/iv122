from Turtle import Turtle
from math import sqrt, ceil

t = Turtle('b_squares')

d = 200
levels = 15

for i in range(levels):
    for i in range(4):
        t.forward(d)
        t.right(90)

    t.forward(d/4)
    t.right(90/5)

    d = sqrt((d/4)**2 + (d - d/4)**2)

t.save()
