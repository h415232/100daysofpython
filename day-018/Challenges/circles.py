from turtle import Turtle, Screen, colormode
import random as r

my_turtle = Turtle()
my_screen = Screen()

my_turtle.speed("fastest")
colormode(255)

radius = 100

def draw_spirograph():
    for angle in range(0, 361, 5):
        rgb = (r.randint(0,255), r.randint(0,255), r.randint(0,255))
        my_turtle.pencolor(rgb)
        my_turtle.circle(radius)
        my_turtle.setheading(angle)

draw_spirograph()


my_screen.exitonclick()