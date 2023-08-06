# Day: 20
# Date: 06-Aug-2023
# Name: Snake (Part 1/2)

from turtle import Screen, Turtle
from snake import Snake
import time

# Global Variable
RES = (600, 600)
game_is_on = True

# Instantiate Screen object
s = Screen()

# Setup Screen
s.setup(width=RES[0], height=RES[1])
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0) # In order to stop screen to animate every movement of turtle

# Instantiate Snake object
snake = Snake()
s.update()

# Make program to listen to inputs
s.listen()
s.onkey(fun=snake.up, key="Up")
s.onkey(fun=snake.down, key="Down")
s.onkey(fun=snake.left, key="Left")
s.onkey(fun=snake.right, key="Right")


while game_is_on:
    snake.move_snake()
    s.update()
    time.sleep(0.1)

s.exitonclick()