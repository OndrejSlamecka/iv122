from Turtle import Turtle

turtle = Turtle('c_koch')

def step(dist, depth):
    if depth == 0:
        turtle.forward(dist)
        return

    step(dist//3, depth - 1)
    turtle.left(60)
    step(dist//3, depth - 1)
    turtle.right(120)
    step(dist//3, depth - 1)
    turtle.left(60)
    step(dist//3, depth - 1)


turtle.left(90)
for i in range(3):
    step(400, 4)
    turtle.rig
    ht(120)

turtle.save()
