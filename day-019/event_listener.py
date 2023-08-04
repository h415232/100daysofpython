from turtle import Turtle, Screen

# Initialize turtle and screen object
t = Turtle()
s = Screen()

# Step Size
step_size = 10

def move_forward():
    t.forward(step_size)

# Initialize screen to "listen" to events on screen
s.listen()

# Move turtle when pressing "space" bar on keyboard
s.onkey(key="space", fun=move_forward)

# To avoid screen to close
s.exitonclick()