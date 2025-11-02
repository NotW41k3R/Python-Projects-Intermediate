import turtle
from turtle import Turtle
FONT = ("Courier", 15, "bold")

class AnswerWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_ans(self,answer,x,y):
        self.goto(x,y)
        self.write(answer,False,'center',FONT)