from turtle import Turtle
import random


def draw_shape(sides, length, color):
    turtle.color(color)
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(length)
        turtle.right(angle)


def draw_star(size, color):
    turtle.color(color)
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)


def random_color():
    return (random.random(), random.random(), random.random())


def main():
    screen = turtle.Screen()
    screen.bgcolor("black")
    turtle.speed(0)

    # Draw multiple shapes with random colors
    for _ in range(36):
        turtle.penup()
        turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
        turtle.pendown()
        sides = random.randint(3, 10)
        length = random.randint(20, 100)
        color = random_color()
        draw_shape(sides, length, color)

    # Draw stars
    for _ in range(10):
        turtle.penup()
        turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
        turtle.pendown()
        size = random.randint(20, 100)
        color = random_color()
        draw_star(size, color)

    turtle.done()


if __name__ == "__main__":
    main()
