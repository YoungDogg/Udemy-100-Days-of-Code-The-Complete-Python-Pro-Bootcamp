from turtle import Turtle, Screen
from random import randint, choice


class MyTurtle(Turtle):
    directions_list = [0, 90, 180, 270]

    def __init__(self, random_move_distance=40):
        super().__init__()
        self.random_move_distance = random_move_distance

    def draw_dot(self,color_list):
        for i in range(10):
            self.color(i)
            self.dot(size=20)
            #set location

    def random_move(self, move_count=20):
        '''
        function: object moving
        parameters: Number of steps of moving
        '''
        self.speed(7)
        self.pen(pensize=10)
        self.error_exception(value=move_count, type=int)
        if move_count > 100:
            move_count = 100
        elif move_count < 0:
            move_count = 0

        self.screen.colormode(255)
        for _ in range(move_count):
            self.color_circling_turtle()
            direction = choice(self.directions_list)
            self.setheading(direction)
            self.forward(self.random_move_distance)

    def circling_circle(self, density):
        self.error_exception(value=density, type=int)
        if density < 1:
            density = 1
        elif density > 180:
            density = 180

        theta = 0
        while theta < 360:
            self.color_circling_turtle()
            self.speed(11)
            self.setheading(theta)
            self.circle(radius=-150)
            theta += density

    def error_exception(self, value, type):
        if not isinstance(value, type):
            raise ValueError(f"{value} must be an {type}")

    def color_circling_turtle(self):
        '''
        function: object coloring
        '''
        color_r = randint(0, 255)
        color_g = randint(0, 255)
        color_b = randint(0, 255)
        self.pencolor(color_r,color_g,color_b)
