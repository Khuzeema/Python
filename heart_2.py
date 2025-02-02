import math
import turtle

# Define heart_x and heart_y functions
def heart_x(t):
    return 16 * math.sin(t)**3

def heart_y(t):
    return 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)

# Function to draw a single heart layer with scaling and color
def draw_heart(turtle_obj, scale_factor, color):
    turtle_obj.penup()  # Lift the pen to start without drawing
    for i in range(300):  # Iterate through 300 steps
        angle = i * (2 * math.pi / 300)  # Convert index to angle in radians
        x = heart_x(angle) * scale_factor
        y = heart_y(angle) * scale_factor
        turtle_obj.goto(x, y)
        turtle_obj.pendown()  # Start drawing after the first point
    turtle_obj.penup()  # Finish the layer

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("3D Red Heart")

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.width(2)

# Draw multiple layers to simulate 3D effect
scale_start = 18
layers = 10
for layer in range(layers):
    # Gradually change the color and scale for each layer
    red_intensity = 1 - (layer / layers)
    color = (red_intensity, 0, 0)  # RGB color for gradient
    screen.colormode(1.0)  # Use RGB colors between 0 and 1
    t.pencolor(color)
    draw_heart(t, scale_start + layer * 0.5, color)

# Finish
turtle.done()
