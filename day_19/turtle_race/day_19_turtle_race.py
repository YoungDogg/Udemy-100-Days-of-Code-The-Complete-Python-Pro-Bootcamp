from turtle import Turtle
from typing import List

class TurtleRaceUnit(Turtle):
    def __init__(self,color:str= "black"):
        super().__init__() # what is the usage of super?
        self.shape("turtle")
        self.color(color)

class TurtleGroup(TurtleRaceUnit):
    turtle_objects: List[TurtleRaceUnit] = []
    turtle_color: List = ["red", "blue", "green", "yellow", "orange", "purple"]
    y_pos = -300
    for color in turtle_color:
        turtle= TurtleRaceUnit()
        turtle.color(color)
        turtle.teleport(x=-400,y=y_pos)
        turtle_objects.append(turtle)
        y_pos += 120

    def __init__(self):
        # self.turtle_objects = []
        # for color in self.turtle_color:
        #     self.turtle_objects.append(TurtleRaceUnit(color))
        pass
    def print(self):
        print(self.turtle_objects)



