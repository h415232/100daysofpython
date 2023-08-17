# Day: 24
# Date: 17-Aug-2023
# Name: [IMPROVEMENT] Snake with Highscore

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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

# Instantiate Snake, Food, and Scoreboard object
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Make program to listen to inputs
s.listen()
s.onkey(fun=snake.up, key="Up")
s.onkey(fun=snake.down, key="Down")
s.onkey(fun=snake.left, key="Left")
s.onkey(fun=snake.right, key="Right")


while game_is_on:
    s.update()
    time.sleep(0.08)
    snake.move_snake()
    scoreboard.show_score()

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.move_food()
        snake.grow()
        scoreboard.add_score()

    # Detect Collision with wall:
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        scoreboard.reset()
        snake.reset()

    # Detect Collision with tail:
    for seg in snake.snake[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()
            break

s.exitonclick()