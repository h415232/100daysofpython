# Day 25
# Date: 18-Aug-2023
# Name: U.S.A. State Game

import turtle
import pandas as pd

# CONSTANTS
MAIN_TITLE = "U.S. States Game"
SUB_TITLE = "/50 States Correct"
PROMPT = "What's another state name?"
IMG_BG = "blank_states_img.gif"
DATA = "50_states.csv"
STATES_TO_LEARN = "states_to_learn.csv"
TEXT_COLOR = "black"

# GLOBAL VARIABLE
correct_guess = 0
states_guess = []

# SETUP THE SCREEN
s = turtle.Screen()
s.title(MAIN_TITLE)
s.addshape(IMG_BG)
turtle.shape(IMG_BG)

# IMPORTING DATA
df = pd.read_csv(DATA)
states = df["state"].to_list()

# Class Definition to enable writing in canvas
class Info(turtle.Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color(TEXT_COLOR)
        self.penup()
        self.hideturtle()

    def display_state(self, data):
        self.goto(data.iloc[0][1], data.iloc[0][2])
        self.write(data.iloc[0][0], align="center", font=("Courier", 12, "normal"))


def update_subtitle():
    return str(correct_guess) + SUB_TITLE

def is_guess_valid(answer):
    return answer in states and answer not in states_guess

def states_to_learn_csv(states_guess):
    states_missed = []
    
    for state in states:
        if state not in states_guess:
            states_missed.append(state)

    with open(STATES_TO_LEARN, mode="w") as f:
        for state in states_missed:
            f.write(state+"\n")

# Instantiate Info Class
info = Info()

while len(states_guess) < 50:
    answer = s.textinput(title=update_subtitle(), prompt=PROMPT).title()

    if is_guess_valid(answer):
        correct_guess += 1
        states_guess.append(answer.title)
        info.display_state(df[df.state == answer])
    elif answer == "Exit":
        states_to_learn_csv(states_guess)
        break
