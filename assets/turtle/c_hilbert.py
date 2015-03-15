from Turtle import Turtle

turtle = Turtle('c_hilbert')

dist = 12

def step(angle, level):
    if level == 0:
        return

    turtle.right(angle)
    step(-angle, level - 1)
    turtle.forward(dist)
    turtle.left(angle)
    step(angle, level - 1)
    turtle.forward(dist)
    step(angle, level - 1)
    turtle.left(angle)
    turtle.forward(dist)
    step(-angle, level - 1)
    turtle.right(angle)

step(90, 5)

turtle.save()
