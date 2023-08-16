from turtle import Turtle

# CONSTANTS
TEXT_COLOR = "black"
LVL_SCORE_POS = (-200,250)
GAMEOVER_POS = (0,0)

class Info(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color(TEXT_COLOR)
        self.penup()
        self.hideturtle()
        self.level = 1

    def update_lvl(self):
        self.level += 1

    def update_info(self):
        self.clear()
        self.goto(LVL_SCORE_POS)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 20, "normal"))
    
    def gameover_info(self):
        self.goto(GAMEOVER_POS)
        self.write("GAMEOVER!", align="center", font=("Courier", 22, "normal"))