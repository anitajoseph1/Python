import turtle
import random

turtle.colormode(255)

def random_color():
    """Generates a random RGB color in (R, G, B) format."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def drawHexagon(t, length):
    t.fillcolor(random_color())  # Set random fill color
    t.begin_fill()
    for _ in range(6):
        t.forward(length)
        t.right(60)
    t.end_fill()
    
def radialPattern(t, length, count):
    for _ in range(count):
        drawHexagon(t, length)
        t.right(360 / count)
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")  # Set background color
radialPattern(t, 100, 12)
turtle.done()