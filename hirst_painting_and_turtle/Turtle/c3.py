import turtle
import random
from turtle import Turtle, Screen

color = ['cyan4', 'red', 'green', 'lightseagreen', 'magenta', 'navy', 'peru', 'purple', 'white', 'yellow', 'salmon', 'turquoise']

toby=Turtle()
toby.shape("turtle")
toby.speed('fastest')
my_screen = Screen()
my_screen.bgcolor('black')
polygon=3
toby.goto(-30,450)
toby.pensize(3)
for i in range(50):
    toby.color(random.choice(color))
    for _ in range(polygon):
        toby.forward(50)
        toby.right(360/polygon)
    polygon += 1

        


my_screen.exitonclick()