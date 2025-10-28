import turtle
import random
from turtle import Turtle, Screen

painting_colors=[(144, 76, 50), (188, 165, 117), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169), (220, 209, 93), (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172), (158, 138, 158), (177, 104, 82), (55, 52, 85), (206, 182, 195), (68, 48, 63), (73, 51, 71), (173, 201, 194), (175, 198, 201), (213, 182, 176), (37, 47, 45)]

toby = Turtle()
toby.hideturtle()
toby.speed('fastest')
turtle.colormode(255)
my_screen = Screen()

toby.penup()
toby.setheading(225)
toby.fd(250)
toby.setheading(0)
size_of_grid=10
for i in range(size_of_grid):
    for j in range(size_of_grid):
        toby.pendown()
        color=random.choice(painting_colors)
        toby.dot(15,color)
        toby.penup()
        forward_dist=25
        toby.fd(forward_dist)
    toby.setheading(90)
    toby.fd(25)
    toby.setheading(180)
    toby.fd(size_of_grid*forward_dist)
    toby.setheading(0)    
my_screen.exitonclick()