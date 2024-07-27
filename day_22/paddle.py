from turtle import Turtle


class Paddle:
    def __init__(self, speed, paddle_size):
        self._speed = speed
        self.size = paddle_size
        self.color = 'white'
        self._paddle = Turtle()
        self._paddle.shapesize(stretch_wid=self.size, stretch_len=.5)
        self._paddle.penup()
        self._paddle.shape("square")
        self._paddle.color(self.color)
        self.score = 0
        self._pos = (0, 0)  # [ ] need to set from child class

    @property
    def paddle(self):
        return self._paddle

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, pos):
        self._pos = pos
        self._paddle.setpos(self._pos)

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, num):
        self._speed = num

    def move(self, direction: int):
        x, y = self._paddle.pos()
        self._paddle.goto(x=x, y=y + (direction * self._speed))

    def hit_ball(self, ball):
        #  Calculate speed and angle upon hit
        pass

    def paddle_distance(self, spot):
        return self._paddle.distance(spot)
