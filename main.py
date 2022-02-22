import turtle
import random

def draw_hexagon():
  for i in range(6):
    turtle.forward(50)
    turtle.left(60)

def draw_honeycomb():
  for i in range(6):
    draw_hexagon()
    turtle.forward(50)
    turtle.right(60)

def figure_8():
  turtle.circle(50)
  turtle.circle(-50)

# Activity 10 - Update the following mandala_flower
# function so that each time the loop runs, the
# turtle changes color to a new random color.
# HINTS:
# - Use turtle.color, and pass in three arguments
#   into the method.
# - Generate three random numbers, one for each
#   value of RGB.
# - Remember that we need to change the color
#   each time we run the loop.
def mandala_flower():

  for i in range(35):

    figure_8()

    turtle.right(10)

# Do not delete the following lines
turtle.speed(0)
turtle.shape("turtle")
turtle.color("orange")

draw_honeycomb()

turtle.penup()
turtle.goto(300, 300)
turtle.pendown()

mandala_flower()