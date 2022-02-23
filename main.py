import turtle

g = turtle.Turtle()
g.forward(100)
g.right(90)
g.forward(50)
g.position()

screen = turtle.Screen()
screen.setup(500,500)
screen.setworldcoordinates(-500,-500,500,500)
art = turtle.Pen()
art.speed(180)
turtle.speed(180)
turtle.bgcolor("black")
colors = ["red", "white", "blue", "green", "orange", "purple", "pink"]
#colors = ["black","black","black","black","black",]
#colors = ["white","white","white","white","white",]
sides = 5
distance = 2
angle = 45



for x in range(20):
  r = 8
  art.pencolor(colors[x%sides])
  art.forward(x*distance/sides + x)
  art.left(360/sides + angle)
  art.width(x*sides/360)
  for i in range(100):
    art.circle(r + i, 35)
    art.pencolor("white")
    turtle.fd(i)
    colors = ["red", "blue", "green", "orange", "purple", "pink"]
    turtle.pencolor(colors[i % sides])
    turtle.left(89.7)
    turtle.speed(90)




