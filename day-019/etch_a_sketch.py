from turtle import Turtle, Screen

# Initialize turtle and screen object
t = Turtle()
s = Screen()

# Set the step size
step_size = 5

# Set the angle size
angle_size = 10

def move_forward():
    t.forward(step_size)

def move_backward():
    t.backward(step_size)

def turn_cw():
    cur_heading = t.heading() - angle_size
    t.setheading(cur_heading)

def turn_ccw():
    cur_heading = t.heading() + angle_size
    t.setheading(cur_heading)

# Initialize listening
s.listen()

s.onkey(key="w", fun=move_forward)
s.onkey(key="s", fun=move_backward)
s.onkey(key="a", fun=turn_cw)
s.onkey(key="d", fun=turn_ccw)
s.onkey(key="c", fun=s.resetscreen)

# To avoid screen to close
s.exitonclick()
