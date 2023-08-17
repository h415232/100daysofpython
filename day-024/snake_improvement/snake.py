# Day: 21
# Date: 07-Aug-2023
# Name: Snake (Part 2/2)

from turtle import Turtle

# GLOBAL VARIABLES
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self) -> None:
        ''' Initializing the Snake Object '''
        self.snake = []
        self.snake_size_init = 3
        self.snake_shape = "square"
        self.snake_color = "white"

        self.create_snake()
        #self.head = self.snake[0]

    def create_snake(self):
        ''' Creating the initial snake '''
        for i in range(self.snake_size_init):
            self.add_segment((-MOVE_DIST*i, 0))
        self.head = self.snake[0]

    def snake_len(self):
        ''' Helper Function to return the current lenght of the Snake '''
        return len(self.snake)

    def up(self):
        ''' Update the direction of snake head to UP '''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        ''' Update the direction of snake head to DOWN '''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        ''' Update the direction of snake head to LEFT '''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        ''' Update the direction of snake head to RIGHT '''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_snake_head(self):
        ''' Move the Snake forward by MOVE_DIST '''
        self.head.forward(MOVE_DIST)

    def move_snake_body(self):
        ''' Move the Body of snake (except head) on the basis of previous position '''
        for i in range(self.snake_len()-1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)

    def move_snake(self):
        ''' Move all of the snake'''
        self.move_snake_body()
        self.move_snake_head()

    def add_segment(self, pos):
        ''' Adding segment to the snake body'''
        seg = Turtle(shape=self.snake_shape)
        seg.penup()
        seg.color(self.snake_color)
        seg.goto(pos)
        self.snake.append(seg)

    def grow(self):
        ''' Growing the snake by 1 segment '''
        self.add_segment(self.snake[-1].position())

    def reset(self):
        ''' Reset the Snake body, and will go to initial state of snake'''
        # Putting the snake body into a different location, so it will not show in screen
        for segment in self.snake: 
            segment.goto(1000,1000)

        self.snake.clear()
        self.create_snake()