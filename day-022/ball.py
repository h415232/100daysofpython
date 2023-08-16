from turtle import Turtle

# CONSTANTS
BALL_SHAPE = "circle"
BALL_COLOR = "white"
BALL_XMOV = 28
BALL_YMOV = 20
BALL_INIT_SPEED = 0.1
BALL_SPEED_DELTA = 0.9
TOLERANCE_X = 300
TOLERANCE_Y = 260

class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.reset_ball()

    def move_ball(self):
        self.goto(x=self.xcor() + self.xmov, y=self.ycor() + self.ymov)

    def bounce_y(self):
        #if abs(self.ycor()) > TOLERANCE_Y:
        self.ymov *= -1

    def bounce_x(self):
        self.xmov *= -1
        self.move_speed *= BALL_SPEED_DELTA

    def reset_ball(self):
        self.goto((0,0))
        self.move_speed = BALL_INIT_SPEED
        self.xmov = BALL_XMOV
        self.ymov = BALL_YMOV
        self.bounce_x()

    