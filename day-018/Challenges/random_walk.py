from turtle import Turtle, Screen
import random as r

# Define a color pallete which will be randomly picked
color_bank = ["#D11141", "#00B159", "#00AEDB", "#F37735", "#FFC425"]

# Define a direction
direction_bank = [90, 270, 0, 180]

# Create the turtle and screen objects
my_turtle = Turtle()
my_screen = Screen()

# Set the thickness of the turtle
my_turtle.width(15)

# Set the fastest speed
my_turtle.speed("fastest")

# Set the step size
step_size = 30

# Set the number of random steps
steps = 1000

# Define Width and Height of screen
WIDTH = my_screen.window_width()
HEIGHT = my_screen.window_height()

def check_border(t):
    x, y = t.pos()

    if x > WIDTH/2:
        my_turtle.penup()
        t.setx(-WIDTH/2)
        my_turtle.pendown()

    if x < -WIDTH/2:
        my_turtle.penup()
        t.setx(WIDTH/2)
        my_turtle.pendown()
        
    if y > HEIGHT/2:
        my_turtle.penup()
        t.sety(-HEIGHT/2)
        my_turtle.pendown()

    if y < -HEIGHT/2:
        my_turtle.penup()
        t.sety(HEIGHT/2)
        my_turtle.pendown()

def rand_walk(steps):  
    for step in range(steps):
        my_turtle.pencolor(r.choice(color_bank))
        my_turtle.setheading(r.choice(direction_bank))
        check_border(my_turtle)
        my_turtle.forward(step_size)
    
    rand_walk(steps)

# Start random walk
rand_walk(steps)

my_screen.exitonclick()