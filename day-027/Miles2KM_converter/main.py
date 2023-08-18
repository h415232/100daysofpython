# Day 27
# Date: 18-Aug-2023
# Name: Mile to KM Converter

from tkinter import *

# CONTSTANTS
LBL_TITLE = "Mile to Km Converter"
LBL_MI = "Miles"
LBL_KM = "Km"
LBL_BUTTON = "Calculate"
LBL_IS_EQ_TO = "is equal to"
WIDTH = 200
HEIGHT = 100
PAD_X = 25
PAD_Y = 15

# Function to trigger when button is clicked
def convert_to_km():
    val = float(input.get())
    lbl3.config(text=str(round(val*1.609344,2)))
    

# Create the initial screen and modify
window = Tk()
window.title(LBL_TITLE)
window.minsize(width=WIDTH, height=HEIGHT)
window["padx"] = PAD_X
window["pady"] = PAD_Y

# Label1
lbl1 = Label(text=LBL_MI)
lbl1.grid(column=2, row=0)

# Label2
lbl2 = Label(text=LBL_IS_EQ_TO)
lbl2.grid(column=0, row=1)

# Label3
lbl3 = Label(text=0)
lbl3.grid(column=1, row=1)

# Label4 
lbl4 = Label(text=LBL_KM)
lbl4.grid(column=2, row=1)

# Text Field
input = Entry(width=10)
input.focus()
input.grid(column=1, row=0)

# Button
button = Button(text=LBL_BUTTON, command=convert_to_km)
button.grid(column=1, row=2)

# To enable window to persist until program is terminated
window.mainloop()