from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

turtle = Turtle()
turtle.shape("turtle")

polygon_num = 10
# formula of sum of inner angles: (n-2) * 180, tri: 1*180, sq: 2*180,
# inner angle of each polygon: (n-2) * 180 * 1/n, tri: 180/3, sq: 360/4
# outer angle? 180 - ((n-2) * 180 * 1/n) = 360/n
num_of_angle = 3

for _ in range(polygon_num):
    rgb_color = [random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)]
    turtle.pencolor((rgb_color[0], rgb_color[1], rgb_color[2]))

    angle = 360 / num_of_angle

    for _ in range(num_of_angle):
        turtle.forward(100)
        turtle.right(angle)

    num_of_angle += 1

screen.exitonclick()
