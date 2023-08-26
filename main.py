import random
from turtle import Turtle, Screen

color = ["red", "green", "yellow", "blue", "purple", "pink", "orange"]
screen = Screen()
is_on = False
screen.setup(width=500, height=320)
user_bet = screen.textinput(title="Make your bed", prompt="Which Turtle will win the race? Enter a color.")

y_position = [-100, -60, -20, 20, 60, 100, 135]

all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.shapesize(1)
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    new_turtle.color(color[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_on = True

while is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 210:
            is_on = False

            winning_color = turtle.pencolor()
            if winning_color == user_bet:

                turtle.write(f"You've won! The {winning_color} turtle is the winner!")

            else:

                turtle.write(f"You've loss! The {winning_color} turtle is the winner!")

        random_speed = random.randint(0, 10)
        turtle.forward(random_speed)
screen.exitonclick()
