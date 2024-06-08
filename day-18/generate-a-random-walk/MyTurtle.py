from turtle import Turtle, Screen
from random import randint, choice


class MyTurtle(Turtle):
    directions_list = [0, 90, 180, 270]

    def __init__(self, distance=40):
        super().__init__()
        self.distance = distance
        self.speed(7)
        self.pen(pensize=10)

    def move(self, move_count=20):
        '''
        function: object moving
        parameters: Number of steps of moving
        '''
        if not isinstance(move_count, int):
            raise ValueError("move_count must be an integer")
        if move_count > 100:
            move_count = 100
        elif move_count < 0:
            move_count = 0

        self.screen.colormode(255)
        for _ in range(move_count):
            self.color_turtle()

            direction = choice(self.directions_list)
            self.setheading(direction)
            self.forward(self.distance)

    def color_turtle(self):
        '''
        function: object coloring
        '''
        color_r = randint(0, 255)
        color_g = randint(0, 255)
        color_b = randint(0, 255)
        self.pencolor(color_r, color_g, color_b)
