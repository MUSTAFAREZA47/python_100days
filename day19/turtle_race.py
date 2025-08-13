from turtle import Turtle, Screen
import random

start_race = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title='Make your bet', prompt='Which turtle win the race? Enter a Color:  ')

color_list = ['yellow', 'orange', 'blue', 'green', 'purple', 'red']
y_coordinates = [100, 50, 0, -50, -100, -150]

all_turtle = []

for color_index in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape('turtle')
    new_turtle.penup()
    new_turtle.color(color_list[color_index])
    new_turtle.goto(x=-230, y=y_coordinates[color_index])
    all_turtle.append(new_turtle)

if user_input:
    start_race = True

while start_race:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winning_color = turtle.penup()
            if winning_color == user_input:
                start_race = False
                print(f"you have won!!! The {winning_color} won the race.")

        turtle.forward(random.randint(1, 11))

screen.exitonclick()
