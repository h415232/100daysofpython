import tkinter

window = tkinter.Tk()

window.title("My first GUI Program") # Adds a title to the top
window.minsize(width=500, height=300) # Sets the minimum resolution

# Label
my_label = tkinter.Label(text="I Am a label", font=("Arial", 24, "bold")) # Initializing a label item
#my_label.pack() # all the items wil be "packed" and put in the center
# pack() is one TKs geometry-management mechanisms
#my_label.place(x=0,y=0) # Another TK geomentry, which puts precision in play
my_label.grid(column=0, row=0) # Another TK geom, which represents elements in a Grid

# Different ways of setting a variable (check documentations)
my_label["text"] = "New Text1" 
my_label.config(text="New Text2")

# Button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

# Another button
button2 = tkinter.Button(text="Another Button")
button2.grid(column=2,row=0)

# Entry [Text Field]
input = tkinter.Entry(width=10)
#input.pack()
input.grid(column=3, row=2)

window.mainloop()
