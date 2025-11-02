import turtle
from turtle import Screen
import pandas as pd
from write import AnswerWriter

screen = Screen()
image = 'f1_tracks.gif'
screen.setup(750,900)
screen.title("Name the Tracks")
screen.addshape(image)
turtle.shape(image)
on_map = AnswerWriter()

track_df = pd.read_csv("tracks.csv")
track_names = track_df.track
track_list = track_names.to_list()

game_is_on = True
while game_is_on:
    answer = screen.textinput(title="Guess the Track", prompt="Name the Country of Tracks").title()
    if answer == 'Exit':
        game_is_on = False
        break
    if answer in track_list:
        track_data = track_df[track_df['track']==answer]
        x = track_data.x.item()
        y = track_data.y.item()
        on_map.write_ans(answer,x,y)
        track_list.remove(answer)

    if answer:
        pass
    else:
        game_is_on = False

turtle.mainloop()

# function used to get coordinates of each track on the image
# def get_mouse_click_coor(x,y):
#    print ([x,y])

# turtle.onscreenclick(get_mouse_click_coor)