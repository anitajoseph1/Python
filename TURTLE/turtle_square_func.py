import turtle
def drawSquare(t, x, y, length):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.shape("turtle")  
    t.color("green")  
    t.speed(1)  
    t.fillcolor("yellow")
    t.begin_fill()
    t.pencolor("blue")  
    for _ in range(4):
        t.forward(length)  
        t.right(90)
    t.end_fill()  
    t.color("green")

t = turtle.Turtle()
drawSquare(t, -50, 50, 100)

turtle.done()
