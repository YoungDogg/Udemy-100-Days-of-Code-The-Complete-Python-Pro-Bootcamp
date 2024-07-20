from player import Player
from opponent import Opponent
from ball import Ball
from screen import Screen


class GameFlow:
    def __init__(self, score_limit, player_speed, opponent_speed, ball_speed, ball_size, paddle_size, width, height):
        self.screen = Screen(width=width, height=height)
        self.player = Player(speed=player_speed, paddle_size=paddle_size, screen=self.screen)
        self.opponent = Opponent(speed=opponent_speed, paddle_size=paddle_size, screen=self.screen)
        self.ball = Ball(speed=ball_speed, size=ball_size)
        self.score_limit = score_limit

    def start_game(self):
        pass

    def update_score(self, winner):
        pass

    def check_game_over(self):
        # determine if the game has ended and display the winner
        pass
