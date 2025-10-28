import turtle
from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(700,450)
screen.bgcolor('black')
colors=["red","orange","yellow","green","blue","purple",]

user_bet=screen.textinput("Place your bets!", "Which turtle will win?, Enter a color")
turtles=[]

for turtle_index in range(0,6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape('turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-330,-100+(turtle_index*50))
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtel in turtles:
        if turtel.xcor()>325:
            is_race_on = False
            if turtel.pencolor() == user_bet:
                print("You've won")
            else:
                print("You Lost")
            break
        random_dist=random.randint(0,10)
        turtel.forward(random_dist)


screen.exitonclick()    