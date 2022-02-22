import turtle

art = turtle.Pen()
art.speed(90)
turtle.bgcolor("black")
#colors = ["red", "blue", "green", "orange", "purple", "pink"]
colors = ["white","white","white","white","white",]
sides = 5
distance = 3
angle = 45

for x in range(360):
  art.pencolor(colors[x%sides])
  art.forward(x*distance/sides + x)
  art.left(360/sides + angle)
  art.width(x*sides/360)