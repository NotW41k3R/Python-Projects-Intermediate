import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("img.gif")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.move,key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    car_manager.move_cars()
    if random.randint(1, 7) == 1:
        car_manager.generate_cars()
    player_y=player.ycor()
    if player_y>=280:
        scoreboard.increase_level()
        player.next_level()
        car_manager.next_level()
    for car in car_manager.cars_on_screen:
        xc=car.xcor()
        yc=car.ycor()
        xp=player.xcor()
        yp=player.ycor()
        if abs(xc-xp)<25 and abs(yc-yp)<15:
            scoreboard.game_over()
            game_is_on = False
    



screen.mainloop()