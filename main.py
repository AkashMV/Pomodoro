from tkinter import *
import math
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
sessions = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global timer
    global sessions
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text=" Pomodoro Timer")
    check.config(text='')
    sessions = 1
    reps = 1
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    global sessions
    if reps % 8 == 0:
        timer_label.config(text="Long Break")
        count_down_func(LONG_BREAK_MIN*60)
        sessions += 1
        session_label.config(text=f"Session: {sessions}")
    elif reps % 2 == 0:
        count_down_func(SHORT_BREAK_MIN*60)
        timer_label.config(text="Short Break")
    else:
#        count_down_func(WORK_MIN*60)
        count_down_func(5)
        timer_label.config(text="Study Time")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down_func(count):
    global reps
    global timer

    minn = math.floor(count/60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{minn}:{sec}")
    if count > 0:
        timer = window.after(1000, count_down_func, count-1)
    else:
        reps += 1
        checks = ''
        if reps % 2 == 0:
            time_comp = math.floor(reps / 2)
            for i in range(time_comp):
                checks += "✅"
        check.config(text=checks)
        playsound(r"C:/Users/nadua/OneDrive/Desktop/Python/Pomodoro/Sounds/notify.wav")
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

session_label = Label(text=f"Session:{sessions}")
session_label.grid(column=2, row=1)
session_label.config(bg=YELLOW, fg=RED, font=(FONT_NAME, 15, "bold"))

timer_label = Label(text="Pomodoro Timer")
timer_label.grid(column=2, row=2)
timer_label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=4)
start_button.config(font=FONT_NAME)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=4)
reset_button.config(font=FONT_NAME)

check = Label()
check.grid(column=2, row=5)
check.config(bg=YELLOW, fg="#019267")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image_file = PhotoImage(file="pomodoro-start/tomato.png")
canvas.create_image(100, 112, image=image_file)
canvas.grid(column=2, row=3)
timer_text = canvas.create_text(100, 130, text=f"00:00", fill="white", font=(FONT_NAME, 35, "bold"))


window.mainloop()
