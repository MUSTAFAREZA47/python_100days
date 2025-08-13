from turtle import Turtle, Screen

# Initializing Turtle
tim = Turtle()
tim.shape('arrow')
tim.pencolor('blue')


def move_forward():
    tim.forward(10)


def move_backward():
    tim.forward(-10)


def clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def anti_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen = Screen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=clockwise)
screen.onkey(key='d', fun=anti_clockwise)
screen.onkey(key='space', fun=clear_screen)


screen.listen()
screen.exitonclick()
