# Day 28
# Date: 19-Aug-2023
# Name: Pomodoro App

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

IMG_DIR = "tomato.png"
WIDTH = 200
HEIGHT = 224
PADDING_X = 100
PADDING_Y = 50

LBL_TITLE = "Pomodoro"
LBL_TIMER = "Timer"
LBL_BTN_START = "Start"
LBL_BTN_RESET = "Reset"
LBL_CHK = "✔"
LBL_SHORT_BREAK = "Break (S)"
LBL_LONG_BREAK = "Break (L)"
LBL_WORK = "Work"
LBL_INIT_TIMER_TEXT = "00:00"

TIME_MIN = 60 # 1 minute = 60 sec
TIME_SEC = 1000 # 1000 milisecond = 1 sec

# ---------------------------- GLOBAL VARIABLE ------------------------------- #
reps = 0
reps_chk = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    '''
      Resets the timer to default, and sets the values back to initial
      Also enables the Start button
    '''
    global reps, reps_chk
    reps = 0
    reps_chk = ""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=LBL_INIT_TIMER_TEXT)
    label_title.config(text=LBL_TIMER)
    label_chk.config(text="")
    btn_start.config(state=ACTIVE) # ACTIVE is inside the TKINTER

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    '''
        Starts the timer and disables the start button to avoid spamming
    '''
    global reps
    reps += 1 

    btn_start.config(state=DISABLED) # DISABLED is inside the TKINER

    work_sec = WORK_MIN * TIME_MIN
    short_break_sec = SHORT_BREAK_MIN * TIME_MIN
    long_break_sec = LONG_BREAK_MIN * TIME_MIN

    if reps%8 == 0:
        count_down(long_break_sec)
        label_title.config(text=LBL_LONG_BREAK, fg=RED)
    elif reps%2 == 0:
        count_down(short_break_sec)
        label_title.config(text=LBL_SHORT_BREAK, fg=PINK)
    else:
        count_down(work_sec)
        label_title.config(text=LBL_WORK, fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    '''
        Count down logic, which also checks if user has completed 1 work loop
        NOTE: 1 work loop = 1 Work + 1 Short or Long break
        NOTE: Every run will be: 1 Work -> 1 Break (S) [3 times] and then 1 Work -> 1 Break (L) [1 Time] then repeat cycle
    '''
    global reps_chk, timer

    count_min = math.floor(count / TIME_MIN)
    count_sec = count % TIME_MIN

    # This ensures that timer will always be on format "MM:SS"
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    if count > 0:
        # If timer is not done, continue to countdown, with count -= 1 
        timer = window.after(TIME_SEC, count_down, count - 1)
    else:
        # If timer has completed, trigger start_timer()
        start_timer()
        if reps%2 == 0:
            # If user completed 1 work loop, show a 1 check mark
            reps_chk += LBL_CHK
            label_chk.config(text=reps_chk)

# ---------------------------- UI SETUP ------------------------------- #
# Setting Window
window = Tk()
window.title(LBL_TITLE)
window.config(padx=PADDING_X, pady=PADDING_Y, bg=YELLOW)

# Setting Canvas to show img
canvas = Canvas(width=WIDTH, height=HEIGHT, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=IMG_DIR)
canvas.create_image(WIDTH/2, HEIGHT/2, image=tomato_img)
timer_text = canvas.create_text(WIDTH/2, HEIGHT/2 + 18, text=LBL_INIT_TIMER_TEXT, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Setting Label Title
label_title = Label(text=LBL_TIMER, bg=YELLOW ,fg=GREEN, font=(FONT_NAME, 40, "normal"))
label_title.grid(column=1, row=0)

# Setting Label Checkmark
label_chk = Label(bg=YELLOW ,fg=GREEN, font=(FONT_NAME, 20, "bold"))
label_chk.grid(column=1, row=3)

# Setting the Button Start
btn_start = Button(text=LBL_BTN_START, highlightbackground=YELLOW, command=start_timer)
btn_start.grid(column=0, row=2)

# Setting the Button Reset
btn_reset = Button(text=LBL_BTN_RESET, highlightbackground=YELLOW, command=reset_timer)
btn_reset.grid(column=2, row=2)

window.mainloop()