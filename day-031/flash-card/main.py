from tkinter import *
import pandas as pd
import random as rand

# CONSTANT VARIABLES
BACKGROUND_COLOR = "#B1DDC6"

WINDOW_TITLE = "Flash Card"
WINDOW_X = 50
WINDOW_Y = 50
CARD_WIDTH = 800
CARD_HEIGHT = 526
CARD_FRONT_DIR = "images/card_front.png"
CARD_BACK_DIR = "images/card_back.png"

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

# Global Variable
word = {}

# Get words from Dictionary
def new_card():
    global word, flip_timer

    # Cancels the job for timer
    window.after_cancel(flip_timer)

    word = rand.choice(word_dict)
    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(title_txt, text="French", fill="black")
    canvas.itemconfig(word_txt, text=word["French"], fill="black")

    # Initiate the job for flip timer
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(title_txt, text="English", fill="white")
    canvas.itemconfig(word_txt, text=word["English"], fill="white")

# Load the French word
df = pd.read_csv(DATA_DIR)
word_dict = df.to_dict(orient="records")

# Creating the window
window = Tk()
window.title(WINDOW_TITLE)
window.config(padx=WINDOW_X, pady=WINDOW_Y, bg=BACKGROUND_COLOR)

# Adding Canvas 
canvas = Canvas(width=CARD_WIDTH, height=CARD_HEIGHT)

# Front Card Image
card_front_img = PhotoImage(file=CARD_FRONT_DIR)

# Back Card Image
card_back_img = PhotoImage(file=CARD_BACK_DIR)

# Create initial image for the card
card = canvas.create_image(CARD_WIDTH/2, CARD_HEIGHT/2, image=card_front_img)

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
unknown_btn = Button(image=cross_image, highlightthickness=0, command=new_card)
unknown_btn.grid(row=1,column=0)

# Known Button
check_image = PhotoImage(file=CHECK_IMG_DIR)
known_btn = Button(image=check_image, highlightthickness=0, command=new_card)
known_btn.grid(row=1,column=1)

# Setup the flip timer
flip_timer = window.after(3000, func=flip_card)

# Get initial word
new_card()

# Make the window persist until closed
window.mainloop()