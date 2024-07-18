from turtle import Turtle


class Paddle:
    def __init__(self, speed, paddle_size):
        self._paddle = Turtle()
        self.speed = speed
        self.size = paddle_size
        self.color = 'white'
        self.score = 0
        self.super_pos = (0,0)  # [ ] need to set from child class

    def set_paddle(self):
        # size and position
        self._paddle.shapesize(stretch_wid=self.size, stretch_len=1)
        self._paddle.setpos(self.super_pos)

    @property
    def get_paddle(self):
        return self._paddle

    def move(self, direction: int):
        # [x] it moves up and down.
        # [x] Need direction parameter
        # [x] Speed required
        x, y = self._paddle.pos()
        self._paddle.penup()
        self._paddle.speed(self.speed)
        self._paddle.goto(x=x, y=direction * y)
        pass

    def hit_ball(self, ball):
        #  Calculate speed and angle upon hit
        pass
