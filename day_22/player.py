from paddle import Paddle
import sys


class Player(Paddle):
    def __init__(self, speed, paddle_size, screen, margin, ball):
        super().__init__(speed, paddle_size)  # need to set pos in parent class
        _margin = margin
        self._screen = screen
        _screen_width, _ = self._screen.get_screen_size
        _screen_x = _screen_width / 2 * (1 - _margin)
        _screen_y = 0
        self.pos = (_screen_x, _screen_y)  # set pos, requiring screen info
        print(f"Player: {self.pos}")

        self._ball = ball
        self.game_flow = None

    @property
    def get_player_speed(self):
        return self.speed

    def move_up(self):
        self.move(direction=1)

    def move_down(self):
        self.move(direction=-1)

    def key_bound(self, game_flow):
        self.game_flow = game_flow
        screen = self._screen.screen
        screen.listen()
        screen.onkeypress(self.move_up, "Up")
        screen.onkeypress(self.move_up, "w")
        screen.onkeypress(self.move_up, "W")
        screen.onkeypress(self.move_down, "Down")
        screen.onkeypress(self.move_down, "s")
        screen.onkeypress(self.move_down, "S")
        # game setting
        screen.onkey(self._ball.initial_move, "r")
        screen.onkey(self._ball.initial_move, "R")
        screen.onkey(self.exit_game, "Escape")

    def exit_game(self):
        print("Exiting game...")
        if self.game_flow:
            self.game_flow.is_over = True
        self._screen.screen.bye()
