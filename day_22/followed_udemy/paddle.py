from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos: tuple):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(pos)
        self.color('white')
        self.speed = 20

    def moveUp(self):
        new_y = self.ycor() + self.speed
        self.goto(self.xcor(), new_y)

    def moveDown(self):
        new_y = self.ycor() - self.speed
        self.goto(self.xcor(), new_y)
