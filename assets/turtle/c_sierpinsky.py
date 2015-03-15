from Turtle import Turtle
import math

turtle = Turtle('c_sierpinsky')

def sierpinsky(dist, level):
    if level == 0:
        for a in [1,2,3]:
            turtle.forward(dist)
            turtle.left(120)
    else:
        sierpinsky(dist / 2, level - 1)
        turtle.forward(dist/2)

        sierpinsky(dist / 2, level - 1)
        for d in [dist/2, dist, dist/2]:
            turtle.forward(d)
            turtle.left(120)

        sierpinsky(dist / 2, level - 1)
        turtle.right(120)
        turtle.forward(dist/2)
        turtle.left(120)

turtle.left(90)
sierpinsky(400, 6)

turtle.save()
