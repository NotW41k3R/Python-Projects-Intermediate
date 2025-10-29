from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 25, "bold")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(0,260)
        self.update_score()
        

    def update_score(self):
        self.write(f"Score: {self.score}",False,ALIGNMENT,FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over.",False,ALIGNMENT,FONT)
        
    