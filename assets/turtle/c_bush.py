from Turtle import Turtle
import math

turtle = Turtle('c_bush')

def step(dist, depth):
    if depth == 0: return

    turtle.forward(dist)

    turtle.left(45)
    step(2*dist//3, depth - 1)

    turtle.right(90)
    step(2*dist//3, depth - 1)

    turtle.left(45)
    turtle.pen_up()
    turtle.back(dist)
    turtle.pen_down()


turtle.left(180)
step(100, 7)

turtle.save()
