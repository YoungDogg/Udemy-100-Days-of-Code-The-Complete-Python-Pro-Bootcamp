from turtle import Turtle, Screen
from typing import List, Tuple
import random


class TurtleRaceUnit(Turtle):
    def __init__(self, color: str = "black"):
        super().__init__()  # Initialize the Turtle base class
        self.shape("turtle")
        self.color(color)

    def teleport_turtle(self, x: int, y: int):
        self.speed(5)
        self.penup()
        self.goto(x, y)
        self.pendown()

    def run_turtle(self):
        # random tutle speed given
        self.speed(random.randint(1, 10))
        self.forward(10)


class TurtleGroup:

    def __init__(self, turtle_num: int = 6):
        self.scn = Screen()  # this is not related to the turtle... how to refactor this one?
        self.scn.colormode(255)

        self.turtle_objects: List[TurtleRaceUnit] = []

        for _ in range(turtle_num):
            color_rgb: List[int] = []
            for _ in range(3):
                color_rgb.append(random.randint(0, 255))
            turtle_color: Tuple = (color_rgb[0], color_rgb[1], color_rgb[2])
            turtle = TurtleRaceUnit()
            turtle.fillcolor(turtle_color)
            turtle.pencolor(turtle_color)
            self.turtle_objects.append(turtle)

    def print_color(self):
        for turtle in self.turtle_objects:
            print(turtle.color()[0])
