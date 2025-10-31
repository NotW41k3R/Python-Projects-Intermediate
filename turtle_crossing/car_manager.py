from turtle import Turtle
import turtle
import random
turtle.addshape('blue.gif')
turtle.addshape('green.gif')
turtle.addshape('red.gif')
turtle.addshape('white.gif')
turtle.addshape('purple.gif')
turtle.addshape('yellow.gif')
SHAPES = ['blue.gif','green.gif','red.gif','white.gif','purple.gif','yellow.gif']

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
LANES = [
    250, 220, 150, 100,     # upper lanes
    0,                      # breathing room
    -100, -140, -200, -240  # lower lanes
]

STARTING_MOVE_DISTANCE = 2.5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars_on_screen=[]
        self.move_dist=STARTING_MOVE_DISTANCE
        new_car=Turtle()
        # new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.shape(SHAPES[random.randint(0,5)])
        new_car.setheading(180)
        new_car.shapesize(stretch_len=2,stretch_wid=1)
        new_car.goto(300,random.choice(LANES))
        self.cars_on_screen.append(new_car)
        self.generate_cars()

    def generate_cars(self):
        new_car=Turtle()
        # new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.shape(SHAPES[random.randint(0,5)])
        new_car.setheading(180)
        new_car.shapesize(stretch_len=2,stretch_wid=1)
        new_car.goto(300,random.choice(LANES))
        while self.cars_on_screen[-1].ycor()==new_car.ycor() and self.cars_on_screen[-1].distance(new_car)<20:
            new_car.goto(300,random.choice(LANES))

        self.cars_on_screen.append(new_car)

    def move_cars(self):
        for car in self.cars_on_screen:
            car.forward(self.move_dist)
            if car.xcor()<-350:
                self.cars_on_screen.remove(car)

    def next_level(self):
        self.move_dist += STARTING_MOVE_DISTANCE
