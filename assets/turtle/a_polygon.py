from Turtle import Turtle
import math

turtle = Turtle('a_polygon')

n = 20
dist = 800 / n

for i in range(n):
    turtle.right(360/n)
    turtle.forward(dist)

turtle.save()
