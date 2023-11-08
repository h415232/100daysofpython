from tkinter import *
import pandas as pd
import random as rand
import os

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

DATA_DFLT_DIR = "data/french_words.csv"
DATA_TO_LEARN_DIR = "data/to_learn.csv"
DATA_LEARNED_DIR = "data/learned.csv"

# Global Variable
word = {}
known = []
unknown = []

# Get words from Dictionary
def new_card():
    global word, flip_timer

    # Cancels the job for timer
    window.after_cancel(flip_timer)

    word = rand.choice(unknown)
    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(title_txt, text="French", fill="black")
    canvas.itemconfig(word_txt, text=word["French"], fill="black")

    # Initiate the job for flip timer
    flip_timer = window.after(3000, func=flip_card)

# Flip the card with the English translation of the Word
def flip_card():
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(title_txt, text="English", fill="white")
    canvas.itemconfig(word_txt, text=word["English"], fill="white")

# If word is known, remove from the current list of words
def known_cmd():
    print("Log: Clicked Known BTN")
    unknown.remove(word)
    known.append(word)

    new_card()

# If word is unknown, add from the list of word to relearn
def unknown_cmd():
    print("Log: Clicked Unknown BTN")
    new_card()

def on_closing():
    print("Log: Clicked the X button, closing the window")
    to_learn_df = pd.DataFrame(unknown)
    learned_df = pd.DataFrame(known)
    
    to_learn_df.to_csv(DATA_TO_LEARN_DIR, header=True, index=False)

    if os.path.isfile(DATA_LEARNED_DIR):
        learned_df.to_csv(DATA_LEARNED_DIR, header=False, index=False, mode='a')
    else:
        learned_df.to_csv(DATA_LEARNED_DIR, header=True, index=False)

    window.destroy()

# Load the French word
if os.path.isfile(DATA_TO_LEARN_DIR):
    print("Log: File 'To Learn' exists!")
    df = pd.read_csv(DATA_TO_LEARN_DIR)
else:
    print("Log: File 'To Learn' doesn't exits, reverting to default")
    df = pd.read_csv(DATA_DFLT_DIR)

# Generate a list of dictionary pairs [{'French':'frenchword', 'English':'englishword'},...]
unknown = df.to_dict(orient="records")

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
unknown_btn = Button(image=cross_image, highlightthickness=0, command=unknown_cmd)
unknown_btn.grid(row=1,column=0)

# Known Button
check_image = PhotoImage(file=CHECK_IMG_DIR)
known_btn = Button(image=check_image, highlightthickness=0, command=known_cmd)
known_btn.grid(row=1,column=1)

# Setup the flip timer
flip_timer = window.after(3000, func=flip_card)

# Get initial word
new_card()

# Save the dataframe when window is closed
window.protocol("WM_DELETE_WINDOW", on_closing)

# Make the window persist until closed
window.mainloop()