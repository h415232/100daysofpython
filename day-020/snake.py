from turtle import Turtle

# GLOBAL VARIABLES
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self) -> None:
        self.snake = []
        self.snake_size_init = 3
        self.snake_shape = "square"
        self.snake_color = "white"

        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        ''' Initializing the Snake Object '''
        for i in range(self.snake_size_init):
            t = Turtle(shape=self.snake_shape)
            t.penup()
            t.color(self.snake_color)
            t.setx(-MOVE_DIST*i)
            self.snake.append(t)

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