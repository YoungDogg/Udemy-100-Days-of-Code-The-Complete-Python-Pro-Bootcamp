from turtle import Turtle


class Paddle:
    def __init__(self,speed):
        self._paddle = Turtle()
        self.speed = speed
        self.size = 10
        self.color = 'white'
        self.score = 0

    @property
    def get_paddle(self):
        return self._paddle

    def hit_ball(self, ball):
        #  Calculate speed and angle upon hit
        pass

    def move(self):
        # Handle the movement of the paddle
        pass
