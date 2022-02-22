import turtle

screen = turtle.Screen()
screen.setup(500,500)
screen.setworldcoordinates(-500,-500,500,500)
art = turtle.Pen()
art.speed(90)
turtle.speed(90)
turtle.bgcolor("black")
colors = ["red", "blue", "green", "orange", "purple", "pink"]
#colors = ["black","black","black","black","black",]
#colors = ["white","white","white","white","white",]
sides = 5
distance = 2
angle = 45



for x in range(160):
  art.pencolor(colors[x%sides])
  art.forward(x*distance/sides + x)
  art.left(360/sides + angle)
  art.width(x*sides/360)



for i in range(10,1800,6):
    turtle.fd(i)
    colors = ["red", "blue", "green", "orange", "purple", "pink"]
    turtle.pencolor(colors[i % sides])
    turtle.left(89.7)
    turtle.speed(90)