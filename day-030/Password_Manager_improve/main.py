# Day 30
# Date: 22-Aug-2023
# Name: Password Generator with GUI [IMPROVED]

from tkinter import *
from tkinter import messagebox
import random as rand
import pyperclip 
import json

# CONSTANT
APP_TITLE = "Simple Password Manager"

C_WIDTH = 200
C_HEIGHT = 200

W_PADDING = 50

TXTBX_WIDTH_M = 21
TXTBX_WIDTH_L = 38

BTN_WIDTH_S = 12
BTN_WIDTH_L = 36

LOGO_DIR = "logo.png"

LBL_WEBSITE = "Website:"
LBL_USERNAME = "Email/Username:"
LBL_PASSWORD = "Password:"

TXT_DFLT_EMAIL = "harveycruzado@gmail.com"

LBL_BTN_PASSWORD = "Generate Password"
LBL_BTN_ADD = "Add"
LBL_BTN_SEARCH = "Search"

MSGBX_ERR = "Error"
MSGBX_ERR_FIELD_INC = "All fields are mandatory, kindly ammend missing parameter(s)"
MSGBX_ERR_NO_PSWD_DB = "No database of passwords!"

NL = "\n"
DATA_DIR = "data.json"

PASS_LENGTH = 12

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    password = ""

    for i in range(PASS_LENGTH):
        char_grp = rand.choice([LETTERS, NUMBERS, SYMBOLS])
        char = rand.choice(char_grp)

        password += char

    input_pass.delete(first=0, last=END)
    input_pass.insert(0, string=password)
    pyperclip.copy(text=password)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_pass():
    try:
        with open(file=DATA_DIR, mode="r") as f:
            data = json.load(f)

            try:
                credentials = data[input_web.get()]
                
                msg_val = f"Email: {credentials['email']} \n \
                            Password: {credentials['password']}"
                
                messagebox.showinfo(title=f"Credentials for: {input_web.get()}", message=msg_val)

            except KeyError as key_err:
                messagebox.showerror(title=MSGBX_ERR, message=f"The website '{key_err}' does not exist in password DB")

    except FileNotFoundError:
        messagebox.showwarning(title=MSGBX_ERR, message=MSGBX_ERR_NO_PSWD_DB)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    web = input_web.get()
    user = input_user.get()
    pswd = input_pass.get()
    
    if len(web) == 0 or len(user) == 0 or len(pswd) == 0:
        messagebox.showerror(title=MSGBX_ERR, message=MSGBX_ERR_FIELD_INC)
    else:
        msg_val = f"These are the details entered: \n \
                    Website: {web} \n \
                    Email: {user} \n \
                    Password: {pswd} \n \
                    \n \
                    Is it ok to save? \
                    "

        is_ok = messagebox.askokcancel(title=web, message=msg_val)

        data_entry = {
            web : {
                "email": user, 
                "password": pswd
            }
        }

        if is_ok:
            try:
                with open(file=DATA_DIR, mode="r") as f:
                    # Reading old data
                    cur_data = json.load(f)
                    # Updating old data with new entry
                    cur_data.update(data_entry)
            except FileNotFoundError:
                cur_data = data_entry
            finally:
                with open(file=DATA_DIR, mode="w") as f:
                    # Saving the updated data to file
                    json.dump(cur_data, f, indent=4)

                    input_web.delete(first=0, last=END)
                    input_pass.delete(first=0, last=END)

# ---------------------------- UI SETUP ------------------------------- #

# Generate Window
window = Tk()
window.title(APP_TITLE)
window.config(padx=W_PADDING, pady=W_PADDING)

# Create Canvas to add the logo
canvas = Canvas(width=C_WIDTH, height=C_HEIGHT, highlightthickness=0)
logo_img = PhotoImage(file=LOGO_DIR)
canvas.create_image(C_WIDTH/2, C_HEIGHT/2, image=logo_img)
canvas.grid(column=1, row=0)

# Create the labels
lbl_web = Label(text=LBL_WEBSITE)
lbl_web.grid(column=0, row=1)

lbl_user = Label(text=LBL_USERNAME)
lbl_user.grid(column=0, row=2)

lbl_pass = Label(text=LBL_PASSWORD)
lbl_pass.grid(column=0, row=3)

# Create the textbox
input_web = Entry(width=TXTBX_WIDTH_M)
input_web.focus()
input_web.grid(column=1, row=1)

input_user = Entry(width=TXTBX_WIDTH_L)
input_user.insert(0, TXT_DFLT_EMAIL)
input_user.grid(column=1, row=2, columnspan=2)

input_pass = Entry(width=TXTBX_WIDTH_M)
input_pass.grid(column=1 , row=3)

# Create the buttons
btn_gen_pass = Button(text=LBL_BTN_PASSWORD, width=BTN_WIDTH_S, command=gen_pass)
btn_gen_pass.grid(column=2, row=3)

btn_add = Button(text=LBL_BTN_ADD, width=BTN_WIDTH_L, command=add_entry)
btn_add.grid(column=1, row=4, columnspan=2)

btn_search = Button(text=LBL_BTN_SEARCH, width=BTN_WIDTH_S, command=search_pass)
btn_search.grid(column=2, row=1)

# To avoid closing the window
window.mainloop()