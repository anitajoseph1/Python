import colorgram
import turtle
import random

turtle.colormode(255)
#rgb_colors = []
#colors = colorgram.extract('spotimage.jpg',30)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

#print(rgb_colors)

color_list = [(247, 241, 234), (249, 228, 236), (224, 242, 230), (243, 236, 68), (183, 75, 21), (228, 154, 7), (234, 72, 134), (200, 163, 114), (216, 228, 238), (202, 131, 191), (116, 168, 241), (220, 231, 5), (76, 173, 37), (71, 103, 230), (125, 205, 126), (45, 111, 39), (75, 37, 30), (151, 74, 156), (60, 100, 153), (241, 162, 196), (244, 55, 28), (187, 28, 12), (203, 13, 78), (140, 216, 237), (248, 170, 166), (76, 67, 47), (148, 185, 244), (159, 212, 173), (253, 10, 4), (42, 90, 32)]

t = turtle.Turtle()
t.speed("fastest")
t.setheading(225)
t.penup()
t.hideturtle()
t.forward(300)
t.setheading(0)
no_of_dots = 100

for dot_count in range(1, no_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)





screen = turtle.Screen()
screen.exitonclick()
