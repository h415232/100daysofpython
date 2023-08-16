from turtle import Turtle

# CONSTANTS:
TXT_COLOR = "white"
L_SCORE_POS = (-100, 200)
R_SCORE_POS = ( 100, 200)

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color(TXT_COLOR)
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1                                                                               

    def r_point(self):
        self.r_score += 1

    def update_scoreboard(self):
        self.clear()
        self.goto(L_SCORE_POS)
        self.write(self.l_score, align="center", font=("Courier", 88, "normal"))
        self.goto(R_SCORE_POS)
        self.write(self.r_score, align="center", font=("Courier", 88, "normal"))