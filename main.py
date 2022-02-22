from turtle import *
import turtle
from turtle import Screen, Turtle
#default shape
turtle.shape("turtle")
tur = turtle.Screen()
tur = turtle.Turtle()
tur.speed(6)
tur.pensize(5)


def hexagon():
# for default shape
    turtle.color("purple")
    turtle.forward(50)

# for circle shape
    turtle.shape("circle")
    turtle.right(60)
    turtle.forward(100)
    turtle.color("purple")

# for triangle shape
    turtle.shape("triangle")
    turtle.right(60)
    turtle.forward(100)
    turtle.color("blue")

# for square shape
    turtle.shape("square")
    turtle.right(60)
    turtle.forward(100)

# for arrow shape
    turtle.shape("arrow")
    turtle.right(60)
    turtle.forward(100)

# for turtle shape
    turtle.shape("turtle")
    turtle.right(60)
    turtle.forward(100)



hexagon()
forward(200)
hexagon()
left(60)
hexagon()
forward(250)
hexagon()
right(180)
