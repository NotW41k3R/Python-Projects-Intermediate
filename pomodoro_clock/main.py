from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

DARK_BLUE = "#0C2B4E"
LIGHTER_BLUE = "#35938D"
DARK_TEAL = "#1D546C"
WHITE = "#F4F4F4"

FONT_NAME = "Courier"
HIGH_FONT = (FONT_NAME,35,"bold")
LOW_FONT = (FONT_NAME,15,"bold")

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

CHECK_MARK = "✓"

REPS = 0
TIMER_STATUS = 1

def checkmark_update():
    checkmark_list.append(CHECK_MARK)
    checkmark_label.config(text=checkmark_list)

def reset_timer():
    canvas.itemconfig(timer_text,text="00:00")
    checkmark_list.clear()
    checkmark_label.config(text=checkmark_list)
    timer_label.config(text="Timer", fg=LIGHTER_BLUE)
    global TIMER_STATUS
    TIMER_STATUS = 0
    global REPS
    REPS = 0

def start_timer():
    global REPS
    REPS += 1
    global TIMER_STATUS
    TIMER_STATUS = 1

    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Focus", fg = DARK_TEAL)
        window.after(work_sec*1000,checkmark_update)

def count_down(count):
    if TIMER_STATUS:
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec=f'0{count_sec}'
        canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
        if count>0:
            window.after(1000,count_down,count-1)
        else:
            window.after(1000,start_timer)
            
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file='tomato.png')

canvas= Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(110,112,image=tomato_img)
timer_text = canvas.create_text(110,130,text="00:00",fill=WHITE,font=HIGH_FONT)
canvas.grid(row=1,column=1 )

timer_label=Label(text="Timer", fg=LIGHTER_BLUE,bg=YELLOW,font=HIGH_FONT)
timer_label.grid(row=0,column=1)

start_button = Button(text="Start", fg=WHITE, bg=LIGHTER_BLUE, font=LOW_FONT,command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset", fg=WHITE, bg=LIGHTER_BLUE, font=LOW_FONT,command=reset_timer)
reset_button.grid(row=2,column=2)

checkmark_list=[]

checkmark_label = Label(text=checkmark_list,fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
checkmark_label.grid(row=2,column=1)

window.mainloop()