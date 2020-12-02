from turtle import Turtle, Screen
import random

color_list = [(194, 165, 113), (135, 166, 193), (52, 102, 145), (145, 90, 45), (223, 208, 119), (187, 156, 34), (11, 23, 57), (61, 21, 9), (185, 145, 166), (140, 178, 151), (69, 119, 79), (61, 13, 26), (129, 77, 103), (136, 27, 12), (13, 38, 21), (22, 52, 133), (175, 187, 219), (169, 101, 132), (121, 27, 44), (92, 152, 102), (93, 120, 179), (213, 177, 197), (22, 94, 63), (181, 101, 88), (168, 207, 180), (66, 153, 17)]

screen = Screen()
screen.colormode(255)
turtle = Turtle()
turtle.pensize(10)
turtle.hideturtle()
space = 50
drawing_size = 10


def random_color():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    return (r, g, b)


def move_right():
    for _ in range(drawing_size):
        turtle.pencolor(random_color())
        turtle.dot()
        turtle.penup()
        turtle.forward(space)
        turtle.pendown()


def draw():
    y_value = space
    for _ in range(drawing_size):
        move_right()
        turtle.penup()
        turtle.goto(0, y_value)
        y_value += space


draw()





screen = Screen()
screen.exitonclick()
