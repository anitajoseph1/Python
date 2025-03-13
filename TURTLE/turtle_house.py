import turtle

# Set up the screen and turtle
#turtle.setup(600, 600)
#screen = turtle.Screen()
#screen.title("Simple House")
turtle.colormode(255)  # Enable RGB color mode
t = turtle.Turtle()
t.speed(1)

# Function to draw a filled rectangle
def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Function to draw a filled triangle
def draw_triangle(x, y, base, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.goto(x + base / 2, y + height)
    t.goto(x + base, y)
    t.goto(x, y)
    t.end_fill()

# Draw the house body (square base)
draw_rectangle(-100, -100, 200, 200, (150, 75, 0))  # Brown walls

# Draw the roof (triangle)
draw_triangle(-100, 100, 200, 100, (200, 0, 0))  # Red roof

# Draw the door (rectangle)
draw_rectangle(-30, -100, 60, 100, (100, 50, 0))  # Dark brown door

# Hide the turtle and finish
t.hideturtle()
turtle.done()
