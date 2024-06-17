from turtle import Turtle

class day_19_sketch_turtle(Turtle):
    def __init__(self):
        super().__init__()

    def move_forward(self):
        self.forward(50)

    def move_backwoard(self):
        self.backward(50)

    def rotate_anti_clock(self):
        self.setheading(self.heading() + 30)

    def rotate_clock(self):
        self.setheading(self.heading() - 30)
