import turtle






g = turtle.Turtle()
#g.forward(100)
#g.right(90)
#g.forward(50)
#g.position()

#screen = turtle.Screen()
#screen.setup(500,500)
#screen.setworldcoordinates(-500,-500,500,500)
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





r = 8
for i in range(500):
  art.circle(r + i, 35)
  art.pencolor(colors[i % sides])
  # turtle.fd(i)
  while i < 50:
    colors = ["black", "white", "gray", "black",  "white"]
    i = i + 1
  if i > 50:
    colors = ["purple", "pink", "blue", "green", "teal", "purple", "pink"]
  # turtle.pencolor(colors[i % sides])
  art.left(89.7)
  art.speed(90)

