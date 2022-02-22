from turtle import *
import turtle
from turtle import Screen, Turtle
#default shape
turtle.shape("turtle")
tur = turtle.Screen()
#tur.bgcolor("white")
tur = turtle.Turtle()
tur.speed(6)
tur.pensize(5)


painting = turtle.Turtle()
painting.speed(55)


def next():
    painting.pencolor("pink")
    for x in range(60):
        painting.forward(60)
        painting.left(133)

    painting.pencolor("cyan")
    for x in range(60):
        painting.forward(100)
        painting.left(13)
        painting.right(50)

def square():
    for a in range(10):
        tur.forward(30)
        tur.right(90)

def rectangle():
    for a in range(10):
        tur.forward(90)
        tur.right(90)


def tetris_piece():
    for a in range(4):
        tur.begin_fill()
        #square()
       # ws.color("black")
        move(painting, -90)
        #rectangle()
        #ws.color("white")
        next()
        #ws.next("pink")
       # ws.end_fill()
       # ws.color("black")
       # ws.forward(30)
        painting.forward(60)
        painting.left(80)

        painting.right(60)
        #move(painting, -90)

def move(t1, len):
    win = turtle.Screen()
    win.bgcolor("white")
    t1.pu()
    t1.fd(len)
    t1.pd()


tetris_piece()

tur.penup()
tur.forward(90)
tur.pendown()