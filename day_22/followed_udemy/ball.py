from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(1, 1)
        self.penup()
        self.setpos(0, 0)
        self.speed = 10

        self.make_toss()

    def make_toss(self):
        new_pos = (self.xcor() + self.speed, self.ycor() + self.speed)
        self.goto(new_pos)

    def move(self, dir_x = 1, dir_y = 1):
        new_pos = (self.xcor() + self.speed, self.ycor() + self.speed)
