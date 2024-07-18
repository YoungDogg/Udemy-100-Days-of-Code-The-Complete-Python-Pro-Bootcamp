from paddle import Paddle


class Player(Paddle):
    def __init__(self, speed, paddle_size):
        super().__init__(speed, paddle_size, pos)   # need to set pos int parent class
    #     set pos, requiring screen info

    @property
    def get_player_speed(self):
        return self._player_speed

    def handle_input(self):
        # keyboard input mapping
        pass