from paddle import Paddle


class Opponent(Paddle):
    def __init__(self, speed, paddle_size, screen, margin):
        super().__init__(speed, paddle_size)
        self._AI_speed = speed
        _margin = margin
        _screen_width, _ = screen.get_screen_size
        _screen_x = -_screen_width / 2 * (1 - _margin)
        _screen_y = 0
        self.pos = (_screen_x, _screen_y)  # set pos, requiring screen info
        print(f"screen size: {screen.get_screen_size}")
        print(f"Opponent: {self.pos}")

    @property
    def get_AI_speed(self):
        return self._AI_speed

    def chase_ball(self, ball):
        # Update paddle position to follow the ball
        pass
