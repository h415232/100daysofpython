from turtle import Turtle, Screen
import random as rand

# Screen Resolution
RES = (500,400)

#  Color Bank
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Initializing Turtles
turtles = []

game_completed = False

def make_turtles():
    for i in range(len(colors)):
        turtles.append(Turtle(shape="turtle"))
        turtles[i].color(colors[i])
        turtles[i].penup()
        turtles[i].goto(x=-((RES[0]/2)-15), y=-140+i*60)
        turtles[i].speed("fast")

def is_finish():
    for i in range(len(turtles)):
        cur_xpos = turtles[i].xcor()
        
        if cur_xpos >= ((RES[0]/2)-50):
            return True
        else:
            return False

def winning_turtle():
    win_turtle = turtles[0]
    for turtle in turtles:
        if turtle.xcor() > win_turtle.xcor():
            win_turtle = turtle

    return win_turtle.pencolor()

def move_turtle(t):
    t.forward(rand.randint(0, 10))

# Setup Screen Resolution: 500x400 pixels
s = Screen()
s.setup(width=RES[0], height=RES[1])

# Setup a text input
user_bet = s.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color")

# Initialize turtles
make_turtles()

while not(game_completed):
    for turtle in turtles:
        move_turtle(turtle)
        game_completed = is_finish()

        if game_completed:
            break

winner = winning_turtle()

if user_bet.lower() == winner:
    print(f"You won the bet! Winning turtle is {winner}")
else:
    print(f"You lost the bet! Winning turtle is {winner}")

# To avoid screen to close
s.exitonclick()
