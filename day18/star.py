from turtle import Turtle, Screen
import random

# screen set up
screen = Screen()
screen.bgcolor('black')

# Initializing Turtle
tim = Turtle()
tim.speed('fastest')
tim.width(2)
tim.hideturtle()

# define a list of colors
contrast_colors = [
    "#00FFFF",
    "#FF00FF",
    "#FFFF00",
    "#00FF00",
    "#FF0000",
    "#FFA500",
    "#0000FF",
    "#800080",
    "#FFFFFF",
    "#40E0D0"
]


def draw_star(size):
    for _ in range(5):
        tim.forward(size)
        tim.right(144)
        tim.forward(size)
        tim.right(144)


def draw_star_pattern():
    for angle in range(0, 360, 30):
        tim.color(random.choice(contrast_colors))
        tim.setheading(angle)
        draw_star(100)


draw_star_pattern()


screen.exitonclick()
