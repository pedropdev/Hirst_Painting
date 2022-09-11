# import colorgram
from random import choice as c
import turtle as t
from turtle import Screen

# rgb_colors = []
#
# colors = colorgram.extract('image.jpg', 50)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

tim = t.Turtle()
tim.penup()
tim.hideturtle()

tim.shape("turtle")
tim.color("SlateBlue")
t.colormode(255)


tim.setheading(225)
tim.forward(250)
tim.setheading(0)
tim.forward(300)

# print(t.pos())

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141),
              (254, 194, 0)]


def hirst_painting():
    """Makes a million dollar painting"""
    x_pos = 123.22
    y_pos = -176.78
    number_of_dots = 0
    while number_of_dots != 100:
        for _ in range(10):
            tim.dot(20, c(color_list))
            tim.forward(50)
        y_pos += 50
        tim.setposition(x_pos,y_pos)
        number_of_dots += 10


hirst_painting()
tim.goto(73.22, -176.78)

screen = Screen()

t.exitonclick()
