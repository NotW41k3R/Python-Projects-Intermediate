import turtle
import random
from turtle import Turtle, Screen

color = ['cyan4', 'red', 'green', 'lightseagreen', 'magenta', 'navy', 'peru', 'purple', 'black', 'yellow', 'salmon', 'turquoise']

toby=Turtle()
toby.shape("turtle")

polygon=3
polygon_angle=[120, 90, 72, 60, 51.43, 45, 40, 36]

for i in range(8):
    toby.color(random.choice(color))
    for _ in range(polygon):
        toby.forward(100)
        toby.right(polygon_angle[i])
    polygon += 1

        

my_screen = Screen()
my_screen.exitonclick()