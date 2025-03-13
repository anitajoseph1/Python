import turtle
import random

# Create turtle object
t = turtle.Turtle()
t.speed(10)  # Fastest speed

# Perform random walk
for _ in range(50):  # 100 steps
    t.forward(20)  # Move forward
    t.right(random.choice([0, 90, 180, 270]))  # Turn randomly
turtle.done()