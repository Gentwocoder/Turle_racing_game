import random
from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
turtle_xcord = [-120, -80, -40, 0, 40, 80, 120]
colors = ["red", "blue", "green", "yellow", "white", "purple", "orange"]
turtles = []

screen.setup(width=600, height=900)b

for i in range(7):
    turtle = Turtle("turtle")
    turtle.setheading(90)
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(turtle_xcord[i], -430)
    turtles.append(turtle)


my_turtle = screen.textinput(title="Turtle", prompt="Enter color of your turtle")

game_is_on = True
while game_is_on:
    picker = random.choice(turtles)
    speed = random.randint(1, 5)
    picker.forward(speed)
    if picker.ycor() >= 428:
        if picker.color()[0] == my_turtle:
            text = Turtle()
            text.color("red")
            text.hideturtle()
            text.write("congratulations you won!", font=("Courier", 20, "cursive"), align="center")
        else:
            text = Turtle()
            text.color("red")
            text.hideturtle()
            text.write(f"you lost the winner is {picker.color()[0]}", font=("Courier", 20, "cursive"), align="center")
        game_is_on = False

screen.exitonclick()
