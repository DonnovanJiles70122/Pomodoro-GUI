from tkinter import *
import time
import math

# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------
# | TIMER RESET |
# ---------------
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

# ------------------
#| TIMER MECHANISM |
# ------------------
def start_timer():

    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    print(reps)

    if reps % 2 == 1:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_seconds)
    elif reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_seconds)
    else:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_seconds)


#------------------------
# | COUNTDOWN MECHANISM |
#------------------------
def count_down(count):

    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_mark.config(text=marks)


#------------
#| UI SETUP |
#------------
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=310, height=310, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="pomodoro.png")
canvas.create_image(150, 155, image=tomato_image)
timer_text = canvas.create_text(150, 160, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#count_down(5) 

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
title_label.config(pady=5)
title_label.grid(column=1, row=0)

start_button = Button(text="Start", bg=GREEN, fg="white", height=2, width=10, font=(FONT_NAME, 15, "bold"), command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", bg=GREEN, fg="white", height=2, width=10, font=(FONT_NAME, 15, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW, font=("bold", 20))
check_mark.grid(column=1, row=3)

window.mainloop()