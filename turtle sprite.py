import turtle

wn = turtle.Screen()

itsy = turtle.Turtle()

leg_count_int = int(input("How Many Legs Does Your Sprite Have?"))

itsy.dot()

for i in range(leg_count_int):

itsy.forward(50)

itsy.backward(50)

itsy.left(360/leg_count_int)

wn.exitonclick()