import turtle
from turtle import Turtle, Screen

toby = Turtle()


toby.shape("turtle")
toby.color("cyan4")

for i in range(4):
    toby.forward(100)
    toby.left(90)

screen = Screen()
screen.exitonclick()