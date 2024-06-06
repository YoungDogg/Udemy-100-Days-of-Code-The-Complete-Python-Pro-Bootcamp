# from turtle import Turtle, Screen
from turtle import Turtle
from random import randint, choice


class MyTurtle(Turtle):
    # class attribute: all objects share this one
    # distance = 10

    # instance attribute: objects have their own ones
    def __init__(self, distance=40):
        super().__init__()
        #     self.distance = distance
        self.distance = distance

    def move(self, move_count=20):
        # self.display()
        directions_list = [0, 90, 180, 270]
        for _ in range(move_count):
            direction = choice(directions_list)
            self.setheading(direction)
            self.forward(self.distance)

            # TODO: make different thick color trace

            # TODO: a little bit faster speed



    # def display(self):
    #     screen = Screen()
    #     screen.mainloop()

