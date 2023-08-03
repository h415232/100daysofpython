from turtle import Screen, Turtle, colormode
import random as r

my_turtle = Turtle()
my_screen = Screen()
colormode(255)

shape_bank = {
    "triangle": [ 3, 120],
    "square":   [ 4, 90],
    "pentagon": [ 5, 72],
    "hexagon":  [ 6, 60],
    "heptagon": [ 7, 51.43],
    "octagon":  [ 8, 45],
    "nonagon":  [ 9, 40],
    "decagon":  [10, 36]
}

size = 90

def draw_dash_line(size):
    for i in range(20):
        my_turtle.penup()
        my_turtle.forward(size)
        my_turtle.pendown()
        my_turtle.forward(size)

def draw_shape(size, shape):
    side = shape_bank[shape][0]
    angle = shape_bank[shape][1]
    my_turtle.pencolor((r.randint(0,255),r.randint(0,255),r.randint(0,255)))

    for i in range(side):
        my_turtle.forward(size)
        my_turtle.right(angle)

#draw_dash_line(10)

for shape in shape_bank:
    draw_shape(size, shape)
    

my_screen.exitonclick()