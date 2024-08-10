from turtle import Turtle


class GameTurtle(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.color('black')
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.setpos(0, -screen.window_height() / 2 + 20)
        self.move_x = 10
        self.move_y = 10

        self.key_binding(screen)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.move_y)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.move_y)

    def move_right(self):
        self.goto(self.xcor() + self.move_x, self.ycor())

    def move_left(self):
        self.goto(self.xcor() - self.move_x, self.ycor())

    def key_binding(self, screen):
        screen.onkey(fun=self.move_up, key='Up')
        screen.onkey(fun=self.move_up, key='w')
        screen.onkey(fun=self.move_down, key='Down')
        screen.onkey(fun=self.move_down, key='s')
        screen.onkey(fun=self.move_right, key='Right')
        screen.onkey(fun=self.move_right, key='d')
        screen.onkey(fun=self.move_left, key='Left')
        screen.onkey(fun=self.move_left, key='a')
