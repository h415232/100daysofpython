from turtle import Turtle
import random as rand

# CONSTANTS
CAR_COLORS = ["red", "blue", "yellow", "orange", "green", "violet"]
RAND_POS_X = (-300,300)
RAND_POS_Y = (-240,240)
STRETCH_LEN = 2
STRETCH_WID = 1
CAR_SHAPE = "square"
INIT_MOVE  = 5
MOVE_DELTA = 10
RESET_XPOS = 300
TOLERANCE_X = -280

class Car(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape(CAR_SHAPE)
        self.color(rand.choice(CAR_COLORS))
        self.goto(x=rand.randint(RAND_POS_X[0], RAND_POS_X[1]),
                  y=rand.randint(RAND_POS_Y[0], RAND_POS_Y[1]))
        self.shapesize(stretch_len=STRETCH_LEN, stretch_wid=STRETCH_WID)
        self.move = INIT_MOVE

    def increase_speed(self):
        self.move += MOVE_DELTA

    def move_car(self):
        if self.on_side():
            self.goto(x=RESET_XPOS ,y=self.ycor())
        self.goto(x=self.xcor() - self.move, y=self.ycor())

    def on_side(self):
        return self.xcor() <= TOLERANCE_X