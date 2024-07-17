from paddle import Paddle


class Player(Paddle):
    def __init__(self, speed):
        super().__init__(speed)
        self._player_speed = speed

    @property
    def get_player_speed(self):
        return self._player_speed

    def handle_input(self):
        # keyboard input mapping
        pass