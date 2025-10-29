import time
from turtle import Turtle
MOVE_DIST=20
STARTING_COORDS = [(0,0),(-20,0),(-40,0)]

class Snake:

    def __init__(self):
        self.snake_body=[]
        self.create_snake()
        self.head=self.snake_body[0]
        self.head.color('brown4')

    def create_snake(self):
        for position in STARTING_COORDS:
            self.add_segment(position)
            
    def add_segment(self,position):
        new_segment=Turtle('square')
        new_segment.penup()
        new_segment.color("saddlebrown")
        new_segment.goto(position)
        self.snake_body.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())
    
    def move(self):
        for seg_num in range(len(self.snake_body)-1,0,-1):
            x=self.snake_body[seg_num-1].xcor()
            y=self.snake_body[seg_num-1].ycor()
            self.snake_body[seg_num].goto(x,y)
        self.head.forward(MOVE_DIST)

    def direction(self,key):
        
        heading=self.head.heading()
        if key=='w' and heading!=270:
            self.head.setheading(90)
        elif key=='a' and heading!=0:
            self.head.setheading(180)
        elif key=='s' and heading!=90:
            self.head.setheading(270)
        elif key=='d' and heading!=180:
            self.head.setheading(0)
