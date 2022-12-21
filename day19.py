from turtle import Turtle,Screen, color
tim= Turtle()
screen=Screen()
import random
# def move_forwards():
#     tim.forward(10)
# def move_backwards():
#     tim.backward(10)
# def turn_left():
#     new_heading=tim.heading()+10
#     tim.setheading(new_heading)
# def turn_right(): 
#     new_heading=tim.heading()-10
#     tim.setheading(new_heading)
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen()

# screen.onkey(move_forwards,"w")

# screen.onkey(move_backwards,"s")

# screen.onkey(turn_left,"a")

# screen.onkey(turn_right,"d")


# screen.exitonclick()

screen=Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="make your bet",prompt="which turtle will winn the rece ? Enter a color:")
colors=["red","orange","yellow","green","blue","purple"]
y_position=[-70,-40,-10,20,50,80]
all_turtles=[]
is_race_on =False

for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230,y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if  winning_color ==user_bet:
              print(f"you've won!the {winning_color}turtle is the winner")
            else:
              print(f"you've won!the {winning_color}turtle is the winner")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()






























