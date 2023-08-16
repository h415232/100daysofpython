# Day: 23
# Date: 16-Aug-2023
# Name: [CAPSTONE] Turtle Crossing Game

from turtle import Screen
from player import Player
from car import Car
from info import Info
import time
import random as rand

# CONSTANTS
WIDTH, HEIGHT = 600, 600
TITLE = "Turtle Crossing"
TIME = 0.01
CAR_COUNT = (10,15)
TOLERANCE_COLLIDE = 20

# Global Variable 
game_is_on = True

# Initialize Screen object
s = Screen()

# Setup Screen
s.setup(width=WIDTH, height=HEIGHT) # Set the screen size
s.title(titlestring=TITLE) # Set the screen title
s.tracer(0) # In order to stop screen to animate every movement of turtle

# Instatiate player object
p = Player()

# Instattiate info object
info = Info()

# Instatiate car objects
cars = []
for i in range(rand.randint(CAR_COUNT[0], CAR_COUNT[1])):
    c = Car()
    cars.append(c)

# Initialize Screen listener
s.listen()
s.onkey(fun=p.up, key="Up")

while game_is_on:
    time.sleep(TIME)
    s.update()
    info.update_info()
    for c in cars:
        # Check collision with Player and Car
        if c.distance(p) <= TOLERANCE_COLLIDE:
            info.gameover_info()
            game_is_on = False
        # Move car
        c.move_car()

    # Check if player is on top of the screen
    if p.on_top():
        info.update_lvl()
        p.reset()
        for c in cars:
            c.increase_speed()

s.exitonclick()