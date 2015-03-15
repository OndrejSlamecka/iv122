from Turtle import Turtle
import math

turtle = Turtle('a_star')

n = 60

for i in range(n):
    turtle.right(360/n)
    if i % 2 == 1:
        turtle.forward(253)
    else:
        turtle.back(253)

turtle.save()
