from paddle import Paddle


class Opponent(Paddle):
    def __init__(self,speed, paddle_size, screen):
        super().__init__(speed, paddle_size)
        self._AI_speed = speed
        _margin = 0.2
        _screen_x = -screen.get_screen[0] /2 * (1+_margin)
        _screen_y = 0
        self.super_pos = (_screen_x,_screen_y)  # set pos, requiring screen info

    @property
    def get_AI_speed(self):
        return self._AI_speed

    def chase_ball(self, ball):
        # Update paddle position to follow the ball
        pass