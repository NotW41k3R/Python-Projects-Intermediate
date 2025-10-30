from turtle import Turtle
FWD_DIST = 3.5
class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=4,stretch_wid=1)
        self.color('brown4')
        self.penup()
        self.setheading(90)

    def move(self):
        self.forward(FWD_DIST)
    

    def direction(self,direction):
        if direction=='Up':
            self.setheading(90)
            self.move()
        elif direction=='Down':
            self.setheading(270)
            self.move()
