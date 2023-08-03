# Day: 18
# Date: 03 & 04-Aug-2023
# Name: Hirsh Dot Painting using Turtle

from turtle import Turtle, Screen, colormode
import random as r

color_list = [(254, 200, 253), (101, 190, 171), (100, 164, 209), (207, 137, 182), (213, 230, 240), (56, 179, 154), (49, 124, 170), (187, 222, 211), (25, 26, 26), (217, 163, 85)]

# Initialize turtle and screen object
t = Turtle()
s = Screen()

# Set Colormode to RGB
colormode(255)

# Set pen up to not draw imaginary line of tracing
t.penup()

# Hide turtle
t.hideturtle()

# Set drawing to be fast
t.speed("fastest")

def move_up():
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)


def paint_hirsh_dot():
    t.setheading(225)
    t.forward(300)
    t.setheading(0)

    for j in range(10):
        for i in range(10):
            t.dot(20, r.choice(color_list))
            t.forward(50)

        move_up()

paint_hirsh_dot()

s.exitonclick()