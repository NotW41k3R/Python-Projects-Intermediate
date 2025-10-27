import turtle
from turtle import Turtle, Screen

toby=Turtle()
toby.shape("turtle")
toby.color("cyan4")

for i in range(10):
    toby.forward(10)
    toby.penup()
    toby.forward(10)
    toby.pendown()

my_screen = Screen()
my_screen.exitonclick()