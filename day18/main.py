import turtle

import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract('hurst-painting.jpg', 10)

rgb_colors_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188),
                   (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49)]

# for i in range(0, 10):
#     color = colors[i]
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors = (r, g, b)
#     rgb_colors_list.append(rgb_colors)

# print(rgb_colors_list)

# Initializing the turtle
turtle.colormode(255)
tim = Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()

# Position the turtle
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
numbers_of_dots = 100

# Create grid of dots
for dot_count in range(1, numbers_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors_list))
    tim.forward(50)
    print(dot_count)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# Create screen object and exit on click
screen = Screen()
screen.exitonclick()

# import random
# from turtle import Turtle, Screen


# my_turtle = Turtle()
# my_turtle.shape('arrow')
# my_turtle.color('green')
# # my_turtle.pensize(3)
# my_turtle.speed('fastest')


# for i in range(15):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()
#     if i == 10:
#         my_turtle.left(90)

# def draw_shape(num_side):
#     angle = 360 / num_side
#     for _ in range(num_side):
#         my_turtle.forward(100)
#         my_turtle.right(angle)
#
# import random
# color = ['black', 'red', 'yellow', 'green', 'pink', 'blue', 'orange', 'purple']
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)
#     my_turtle.pencolor(random.choice(color))


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
#
# #
# #
# # angle = [0, 90, 180, 270]
# color = ['black', 'red', 'yellow', 'green', 'pink', 'blue', 'orange', 'purple']


#
# for _ in range(500):
#     my_turtle.color(random_color())
#     my_turtle.forward(30)
#     my_turtle.setheading(random.choice(angle))

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         my_turtle.color(random.choice(color))
#         my_turtle.circle(100)
#         my_turtle.setheading(my_turtle.heading() + size_of_gap)
#
#
# draw_spirograph(5)
#
# screen = Screen()
# screen.exitonclick()
