# Date: 15-Aug-2023
# Day: 22
# Name: Ping-pong game

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# CONSTANTS
WIDTH = 800
HEIGHT = 600
P1_POS = (350,0)
P2_POS = (-350,0)
TOLERANCE_Y = 260
TOLERANCE_X = 310
TOLERANCE_PAD = 50
BGCOLOR = "black"
TITLE = "Pong"

# GLOBAL VAR
game_is_on = True

# Initiate screen
s = Screen()

# Setup Screen
s.setup(width=WIDTH, height=HEIGHT) # Set the screen size
s.bgcolor(BGCOLOR) # Set the screen background color
s.title(titlestring=TITLE) # Set the screen title
s.listen() # Initialize screen listener
s.tracer(0) # In order to stop screen to animate every movement of turtle

# Initialize the Paddles
rp = Paddle(P1_POS)
lp = Paddle(P2_POS)

# Initialize the Ball
b = Ball()

# Initialize the Scoreboard
score = Scoreboard()

# Event Listeners
s.onkeypress(fun=rp.up, key="Up")
s.onkeypress(fun=rp.down, key="Down")
s.onkeypress(fun=lp.up, key="w")
s.onkeypress(fun=lp.down, key="s")

while game_is_on:
    time.sleep(b.move_speed)
    s.update() 
    b.move_ball()

    if abs(b.ycor()) > TOLERANCE_Y:
        b.bounce_y()

    if abs(b.xcor()) > TOLERANCE_X:
        if abs(b.distance(rp)) < TOLERANCE_PAD or abs(b.distance(lp)) < TOLERANCE_PAD:
            b.bounce_x()
        else:
            if abs(b.distance(rp)) > TOLERANCE_X:
                b.reset_ball()
                score.r_point()
            elif abs(b.distance(lp)) > TOLERANCE_X:
                b.reset_ball()
                score.l_point()

    score.update_scoreboard()

s.exitonclick()