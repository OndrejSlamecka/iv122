from Turtle import Turtle

dist = 35

turtle = Turtle('b_circles')

for i in range(12):
    for j in range(12):
        turtle.right(360/12)
        turtle.forward(dist)
    turtle.right(360/12)


turtle.save()
