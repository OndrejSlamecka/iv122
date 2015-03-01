from Turtle import Turtle
import math

dist = 100
golden_ratio = (1 + 5 ** 0.5) / 2

turtle = Turtle('b_pentagram')

turtle.right(90/5)

for i in range(5):
    turtle.right(360/5)
    turtle.forward(dist)

turtle.right(90 + 90/5)

for i in range(5):
    turtle.right((180 - (360/5)) / 3)
    if i % 2 == 0:
        turtle.forward(dist*golden_ratio)
    else:
        turtle.back(dist*golden_ratio)

turtle.save()
