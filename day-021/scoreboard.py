from turtle import Turtle

# CONSTANTS
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self) -> None:
        ''' Initializing the Scoreboard class, inheriting from Turtle class'''
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)

        self.show_score()
        self.ht()

    def add_score(self):
        ''' Adding score to scoreboard with increments of 1 '''
        self.score += 1

    def show_score(self):
        ''' Showing the updated score '''
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        ''' Informing user that game is over '''
        self.goto(0, 0)
        self.write("Game over!", align=ALIGNMENT, font=FONT)