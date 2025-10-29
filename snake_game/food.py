from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("darkslategray")
        self.penup()
        self.shapesize(stretch_len=0.8,stretch_wid=0.8)
        self.speed("fastest")
        self.regenerate()

    def regenerate(self):
        x=random.randint(-275,275)
        y=random.randint(-275,275)
        self.goto(x,y)