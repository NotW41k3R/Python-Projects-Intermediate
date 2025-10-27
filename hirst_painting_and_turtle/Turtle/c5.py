import turtle
import random
from turtle import Turtle, Screen

turtle.colormode(255)
toby=Turtle()
my_screen = Screen()
toby.shape("classic")
toby.speed("fastest")
toby.pensize(5)

my_screen.bgcolor('black')

def move():
    toby.circle(200)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

for _ in range(91):
    toby.color(random_color())
    move()
    toby.right(4)

my_screen.exitonclick()