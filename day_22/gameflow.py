from player import Player
from opponent import Opponent
from ball import Ball
from gamescreen import GameScreen
import time


class GameFlow:
    def __init__(self, score_limit,
                 player_speed, opponent_speed, ball_speed,
                 ball_size, paddle_size,
                 width, height, paddles_margin):
        self.screen = GameScreen(width=width, height=height)
        self.ball = Ball(speed=ball_speed, size=ball_size, screen=self.screen)
        self.player = Player(speed=player_speed, paddle_size=paddle_size, screen=self.screen, margin=paddles_margin,
                             ball=self.ball)
        self.opponent = Opponent(speed=opponent_speed,
                                 paddle_size=paddle_size, screen=self.screen, margin=paddles_margin)
        self.score_limit = score_limit

    def start_game(self):
        self.player.key_bound()
        is_over = False
        while not is_over:
            self.ball.move()
            self.screen.screen.update()
            time.sleep(.01)

    def update_score(self, winner):
        pass

    def check_game_over(self):
        # determine if the game has ended and display the winner
        pass
