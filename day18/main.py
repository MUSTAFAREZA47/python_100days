import random
from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape('arrow')
my_turtle.color('green')
# my_turtle.pensize(3)
my_turtle.speed('fastest')


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


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


#
#
# angle = [0, 90, 180, 270]
color = ['black', 'red', 'yellow', 'green', 'pink', 'blue', 'orange', 'purple']


#
# for _ in range(500):
#     my_turtle.color(random_color())
#     my_turtle.forward(30)
#     my_turtle.setheading(random.choice(angle))

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        my_turtle.color(random.choice(color))
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
