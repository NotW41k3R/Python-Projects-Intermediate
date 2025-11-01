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
        with open('data.txt') as highscore:
            self.high_score = int(highscore.read())
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",False,ALIGNMENT,FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        if self.score>self.high_score:
            with open('data.txt', mode="w") as highscore:
                highscore.write(f"{self.score}")
        self.write(f"Game Over.",False,ALIGNMENT,FONT)
        
    