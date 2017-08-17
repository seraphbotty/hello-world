import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

for color in ('yellow', 'red', 'purple', 'blue'):
    alex.color(color)     #uses each color in the list and converts the turtle (alex) into a new color
    alex.forward(50)
    alex.left(90)

wn.exitonclick()