import turtle

tanenbaum = turtle.Turtle()
ws = turtle.Screen()
tanenbaum.hideturtle()
tanenbaum.speed(20)

for i in range(500):
    tanenbaum.forward(i)
    tanenbaum.right(110)

ws.exitonclick()