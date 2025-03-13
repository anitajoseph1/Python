import turtle
t = turtle.Turtle()
t.shape("turtle")  # Set turtle shape to "turtle"
t.color("green")  # Set turtle color to green
t.speed(1)  # Set the turtle speed to the slowest

# Begin filling the square with yellow
t.fillcolor("yellow")
t.begin_fill()
t.pencolor("blue")  # Set the border color to blue
for _ in range(4):
    t.forward(100)  # Move forward by 100 units
    t.right(90)  # Turn right by 90 degrees

t.end_fill()  # End filling the square

# Reset the turtle’s color after filling the square
t.color("green")
turtle.done()