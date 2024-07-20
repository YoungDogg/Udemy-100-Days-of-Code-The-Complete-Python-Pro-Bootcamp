from turtle import Turtle


class Paddle:
    def __init__(self, speed, paddle_size):
        self._paddle = Turtle()
        self.speed = speed
        self.size = paddle_size
        self.color = 'white'
        self.score = 0
        self._pos = (0, 0)  # [ ] need to set from child class

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, pos):
        self._pos = pos

    @property
    def paddle(self):
        return self._paddle

    @paddle.setter
    def paddle(self):
        # size and position
        self._paddle.shapesize(stretch_wid=self.size, stretch_len=1)

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
