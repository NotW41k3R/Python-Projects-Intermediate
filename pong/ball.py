from turtle import Turtle
import random
FWD_DIST = 3.5
ANGLES=[30,-30,40,-40,45,-45,50,-50,120,-120,130,-130,135,-135,140,-140]
STARTING_ANGLE = random.choice(ANGLES)
SPEEDS = [8,9,10]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('red')
        self.setheading(STARTING_ANGLE)
        self.speed('fastest')
        self.move_speed=0.025/2

    def move(self):
        self.forward(FWD_DIST)

    def bounce_x(self):
        self.setheading(180-self.heading()-random.uniform(-3, 3))

    def bounce_y(self):
        self.setheading(360-self.heading()-random.uniform(-2, 2))
        self.move_speed *= 0.9

    def refresh(self):
        self.goto(0,random.randint(-100,100))
        self.move_speed=0.025/2
        self.setheading(random.choice(ANGLES))