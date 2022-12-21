# from turtle import Turtle ,Screen, color, pensize
# tim=Turtle()
# # import random

# # my_turtle.shape("turtle")
# # my_turtle.color("red")
# # my_turtle.forward(100)
# # my_turtle.right(90)
# # my_turtle.forward(100)
# # my_turtle.right(90)
# # my_turtle.forward(100)
# # my_turtle.right(90)
# # for _ in range(4):
# #  my_turtle.forward(100)
# #  my_turtle.right(90)
# # tim=t.Turtle()
# # for _ in  range (15):
# #     tim.penup()
# #     tim.forward(10)
# #     tim.pendown()
# #colors=("CornflowerBlue","DarkOrchid","IndianRed")
# # def draw_shape(num_sides):
# #     angle=360/num_sides
# #     for _ in  range(num_sides):
# #         tim.forward(100)
# #         tim.right(angle)

# # for  shape_side in range(3,11):
# #     tim.color(random.choice(colors))
# # #     draw_shape(shape_side)
# # directions=[0,90,180,270]
# # tim.pensize(15)
# # #tim.pencolor('r','g','b')
# # tim.speed("fastest")
# # for _ in range (200):
# #     #tim.color(random.choice(colors))
# #     tim.forward(30)
# #     tim.setheading(random.choice(directions))


# tim.circle(100)










# screen=Screen()
# Screen.exitonclick()



import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()







