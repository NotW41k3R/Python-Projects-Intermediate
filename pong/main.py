import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

UP_BORDER = 250
BOTTOM_BORDER = 250

screen = Screen()
screen.setup(800,600)

screen.bgpic('image.png')
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle()
paddle1.goto(-380,0)
paddle2 = Paddle()
paddle2.goto(370,0)
screen.update()

scoreboard = Scoreboard()

ball = Ball()

screen.listen()
screen.onkey(lambda: paddle1.direction('Up'), 'w')
screen.onkey(lambda: paddle1.direction('Down'), 's')
screen.onkey(lambda: paddle2.direction('Up'), 'Up')
screen.onkey(lambda: paddle2.direction('Down'), 'Down')

player1_score=0
player2_score=0

game_is_on = True
while game_is_on:
    y1=paddle1.ycor()
    y2=paddle2.ycor()
    x1=paddle1.xcor()
    x2=paddle2.xcor()
    yb=ball.ycor()
    xb=ball.xcor()
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Collision with Top and Bottom walls
    if y1<=UP_BORDER and y1>=-BOTTOM_BORDER:
        paddle1.move()
        
    if y2<=UP_BORDER and y2>=-BOTTOM_BORDER:
        paddle2.move()

    if yb>280:
        ball.sety(280)
        ball.bounce_y()
    elif yb<-280:
        ball.sety(-280)
        ball.bounce_y()

    # Collision with Paddles
    if abs(xb-x1)<15 and abs(yb-y1)<40:
        ball.bounce_x()
        ball.setx(-365)
    
    if abs(xb-x2)<15 and abs(yb-y2)<40:
        ball.bounce_x()
        ball.setx(355)

    # Collision with wall behind paddles
    if ball.xcor()>380:
        ball.refresh()
        scoreboard.increase_p1()
        time.sleep(0.8)
    if ball.xcor()<-390:
        ball.refresh()
        scoreboard.increase_p2()
        time.sleep(0.8)


screen.mainloop()