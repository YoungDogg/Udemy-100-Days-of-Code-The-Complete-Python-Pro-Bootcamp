from turtle import Turtle


class Day19SketchTurtle(Turtle):
    def __init__(self):
        super().__init__()

    def move_forward(self) -> None:
        self.forward(50)

    def move_backward(self) -> None:
        self.backward(50)

    def rotate_anti_clock(self) -> None:
        self.setheading(self.heading() + 30)

    def rotate_clock(self) -> None:
        self.setheading(self.heading() - 30)
