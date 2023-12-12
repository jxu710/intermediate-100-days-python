import turtle
from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race, enter a clor:")
colors=["red","orange","yellow","green","blue","purple"]
all_turtle= []

position_x = -230
position_y = -150
for i in range (len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(position_x, position_y)
    position_y += 50
    all_turtle.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        random_speed = random.randint(0,10)
        turtle.forward(random_speed)
        if turtle.xcor()> 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"you've won ! the {winner} is the winning turtle")
            else:
                print(f"You lost, the {winner} is the winning one")




screen.exitonclick()


