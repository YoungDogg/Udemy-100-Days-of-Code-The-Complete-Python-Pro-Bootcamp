from paddle import Paddle


class Opponent(Paddle):
    def __init__(self,speed, paddle_size):
        super().__init__(speed, paddle_size)
        self._AI_speed = speed

    @property
    def get_AI_speed(self):
        return self._AI_speed

    def chase_ball(self, ball):
        # Update paddle position to follow the ball
        pass