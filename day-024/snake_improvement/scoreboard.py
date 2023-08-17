from turtle import Turtle

# CONSTANTS
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
HIGHSCORE_FILE = "data.txt"


class Scoreboard(Turtle):

    def __init__(self) -> None:
        ''' Initializing the Scoreboard class, inheriting from Turtle class'''
        super().__init__()
        self.score = 0
        self.read_high_score()
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
        self.write(f"Score: {self.score} Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

        self.score = 0
        self.show_score()

    def save_high_score(self):
        with open(HIGHSCORE_FILE, mode="w") as f:
            f.write(str(self.high_score))

    def read_high_score(self):
        with open(HIGHSCORE_FILE, mode="r") as f:
            self.high_score = int(f.read())

    # def game_over(self):
    #     ''' Informing user that game is over '''
    #     self.goto(0, 0)
    #     self.write("Game over!", align=ALIGNMENT, font=FONT)