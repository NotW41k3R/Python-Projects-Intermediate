import turtle
from turtle import Turtle, Screen

marker = Turtle()
canvas = Screen()

def move_fd():
    marker.forward(10)

def move_bk():
    marker.backward(10)

def clockwise():
    marker.right(5)

def anticlockwise():
    marker.left(5)

def clear_canvas():
    marker.clear()
    marker.penup()
    marker.home()
    marker.pendown()

canvas.listen()
canvas.onkey(key="w", fun=move_fd)
canvas.onkey(key="s", fun=move_bk)
canvas.onkey(key="a", fun=anticlockwise)
canvas.onkey(key="d", fun=clockwise)
canvas.onkey(key="c", fun=clear_canvas)



canvas.mainloop()