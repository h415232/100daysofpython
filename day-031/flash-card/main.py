from tkinter import *
import pandas as pd
import random as rand

# GLOBAL VARIABLES
BACKGROUND_COLOR = "#B1DDC6"

WINDOW_TITLE = "Flash Card"
WINDOW_X = 50
WINDOW_Y = 50
CARD_WIDTH = 800
CARD_HEIGHT = 526
CARD_FRONT_DIR = "images/card_front.png"

TITLE_TXT_PLACEHOLDER = "Title"
TITLE_TXT_CONFIG = ("Ariel", 40, "italic")
TITLE_TXT_XPOS = 400
TITLE_TXT_YPOS = 150

WORD_TXT_PLACEHOLDER = "Word"
WORD_TXT_CONFIG = ("Ariel", 60, "bold")
WORD_TXT_XPOS = 400
WORD_TXT_YPOS = 263

TXT_COLOR_FILL = '#000000'

CROSS_IMG_DIR = "images/wrong.png"
CHECK_IMG_DIR = "images/right.png"

DATA_DIR = "data/french_words.csv"

# Get words from Dictionary
def new_word():
    word = rand.choice(word_dict)
    canvas.itemconfig(title_txt, text="French")
    canvas.itemconfig(word_txt, text=word["French"])

# Load the French word
df = pd.read_csv(DATA_DIR)
word_dict = df.to_dict(orient="records")

# Creating the window
window = Tk()
window.title(WINDOW_TITLE)
window.config(padx=WINDOW_X, pady=WINDOW_Y, bg=BACKGROUND_COLOR)

# Adding Canvas 
canvas = Canvas(width=CARD_WIDTH, height=CARD_HEIGHT)

# Front Card
card_front_img = PhotoImage(file=CARD_FRONT_DIR)
canvas.create_image(CARD_WIDTH/2, CARD_HEIGHT/2, image=card_front_img)

# Title Txt
title_txt = canvas.create_text(TITLE_TXT_XPOS, 
                               TITLE_TXT_YPOS, 
                               text=TITLE_TXT_PLACEHOLDER, 
                               font=TITLE_TXT_CONFIG, 
                               fill=TXT_COLOR_FILL)

# Word Txt
word_txt = canvas.create_text(WORD_TXT_XPOS, 
                              WORD_TXT_YPOS, 
                              text=WORD_TXT_PLACEHOLDER, 
                              font=WORD_TXT_CONFIG, 
                              fill=TXT_COLOR_FILL)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0, columnspan=2)

# Unknown Button
cross_image = PhotoImage(file=CROSS_IMG_DIR)
unknown_btn = Button(image=cross_image, highlightthickness=0, command=new_word)
unknown_btn.grid(row=1,column=0)

# Known Button
check_image = PhotoImage(file=CHECK_IMG_DIR)
known_btn = Button(image=check_image, highlightthickness=0, command=new_word)
known_btn.grid(row=1,column=1)

# Get initial word
new_word()

# Make the window persist until closed
window.mainloop()