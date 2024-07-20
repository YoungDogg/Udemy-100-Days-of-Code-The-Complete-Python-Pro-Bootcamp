from paddle import Paddle

class Player(Paddle):
    def __init__(self, speed, paddle_size, screen):
        super().__init__(speed, paddle_size)  # need to set pos in parent class
        _margin = 0.2
        _screen_x = screen.get_screen[0] / 2 * (1 - _margin)
        _screen_y = 0
        self.pos = (_screen_x, _screen_y)  # set pos, requiring screen info

    @property
    def get_player_speed(self):
        return self.speed

    def handle_input(self):
        # keyboard input mapping
        pass
