from turtle import Turtle

# CONSTANTS
MOVE = 40
STRECH_LEN = 1
STRECH_WID = 5
PADDLE_SHAPE = "square"
PADDLE_COLOR = "white"

class Paddle(Turtle):
    def __init__(self, init_pos) -> None:
        super().__init__()
        self.penup()
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_len=STRECH_LEN, stretch_wid=STRECH_WID)
        self.goto(init_pos)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE)

    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVE)