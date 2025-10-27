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

def move(direction_no):
    if direction_no==0:
        pass
    elif direction_no==1:
        toby.left(90)
    elif direction_no==2:
        toby.right(90)
    elif direction_no==3:
        toby.left(180)
    toby.forward(20)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

for _ in range(1000):
    toby.color(random_color())
        
    move(random.randint(0,3))
    
my_screen.exitonclick()