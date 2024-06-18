from turtle import Turtle

class TurtleRaceUnit(Turtle):
    def __init__(self,color):
        super().__init__() # what is the usage of super?
        self.shape("turtle")
        self.color(color)

# TODO: Make a class for turtle group