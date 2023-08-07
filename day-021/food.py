from turtle import Turtle
import random as rand

class Food(Turtle):

    def __init__(self) -> None:
        ''' Initializing Food class, inheriting from Turtle Class '''
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.move_food()


    def move_food(self):
        ''' Moving the food to a random location within the canvas '''
        # since the shape will be 10x10 (20 px), to avoid walls, we -20
        init_x = rand.randint(-280, 280) 
        init_y = rand.randint(-280, 280)

        self.goto(x=init_x, y=init_y)