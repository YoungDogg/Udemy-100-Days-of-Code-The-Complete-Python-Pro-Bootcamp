from paddle import Paddle


class Player(Paddle):
    def __init__(self, speed, paddle_size, screen, margin):
        super().__init__(speed, paddle_size)  # need to set pos in parent class
        _margin = margin
        self._screen = screen
        _screen_width, _ = self._screen.get_screen_size
        _screen_x = _screen_width / 2 * (1 - _margin)
        _screen_y = 0
        self.pos = (_screen_x, _screen_y)  # set pos, requiring screen info
        print(f"Player: {self.pos}")

    @property
    def get_player_speed(self):
        return self.speed

    def handle_input(self):
        # keyboard input mapping
        pass

    def move_up(self):
        self.move(direction=1)
        # print("move up")
        # logging.info("move_up")

    def move_down(self):
        self.move(direction=-1)
        # print("move down")

    def key_bound(self):
        screen = self._screen.screen
        screen.listen()
        screen.onkeypress(self.move_up, "Up")
        screen.onkeypress(self.move_up, "w")
        screen.onkeypress(self.move_up, "W")
        screen.onkeypress(self.move_down, "Down")
        screen.onkeypress(self.move_down, "s")
        screen.onkeypress(self.move_down, "S")
