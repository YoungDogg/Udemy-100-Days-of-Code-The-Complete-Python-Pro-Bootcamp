from turtle import Turtle
import random

'''
attributes: shape, size, colors, speed
fixed : shape, size
randomized : colors, speed

methods: spawning random position, moving one way
'''

MARGIN = 20


class Car(Turtle):

    def __init__(self, screen, difficulty):
        super().__init__()
        self.__color = ["red", "green", "blue", "cyan", "magenta",
                        "gray", "orange", "purple", "brown", "pink", "lime", "indigo", "violet"]
        self.__pick_color = random.randrange(0, len(self.__color))
        self.shape('square')
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.setheading(90)
        self.color(self.__color[self.__pick_color])
        self.__speed = random.randrange(1, 10) * (1 / 10) * difficulty
        self.penup()

        self.__direction = 1 if random.choice([True, False]) else -1
        scn_x = (screen.window_width() / 2) * self.__direction
        scn_y = random.randrange(-screen.window_height() / 2 + MARGIN, screen.window_height() / 2 - MARGIN)
        self.setpos(scn_x, scn_y)


    def move_car(self):
        self.goto(self.xcor() + (self.__speed * -self.__direction), self.ycor())
