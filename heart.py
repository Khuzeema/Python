import math
import turtle

# Define heart_x and heart_y functions
def heart_x(t):
    return 16 * math.sin(t)**3

def heart_y(t):
    return 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)

# Set up the screen
screen = turtle.Screen()
screen.bgcolor('black')
screen.title('Red Heart')

# Set up the turtle
t = turtle.Turtle()
t.speed(5)
t.width(2)
t.pencolor('red')

# Scale factor for the heart shape
scale_factor = 18

# Draw the heart shape
t.penup()  # Lift the pen to start without drawing
for i in range(300):  # Iterate through 300 steps
    angle = i * (2 * math.pi / 300)  # Convert index to angle in radians
    x = heart_x(angle) * scale_factor
    y = heart_y(angle) * scale_factor
    t.goto(x, y)
    t.pendown()  # Start drawing after the first point

# Finish
turtle.done()
