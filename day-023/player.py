from turtle import Turtle

# CONSTANTS
INIT_POS = (0, -280)
MOVE = 10
SHAPE = "turtle"
NORTH = 90
TOLERANCE_Y = 280

class Player(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.setheading(NORTH)
        self.shape(SHAPE)
        self.reset()

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE)

    def on_top(self):
        return self.ycor() >= TOLERANCE_Y
    
    def reset(self):
        self.goto(INIT_POS)