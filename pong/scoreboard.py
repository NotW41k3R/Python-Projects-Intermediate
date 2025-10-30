from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 25, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score_p1=0
        self.score_p2=0
        self.goto(0,250)
        self.update_score()

    def update_score(self):
        self.write(f"{self.score_p1}            {self.score_p2}",False,ALIGNMENT,FONT)

    def increase_p1(self):
        self.clear()
        self.score_p1 += 1
        self.update_score()

    def increase_p2(self):
        self.clear()
        self.score_p2 += 1
        self.update_score()