from player import Player
from opponent import Opponent
from ball import Ball


class GameFlow:
    def __init__(self, score_limit,player_speed, opponent_speed, ball_speed,ball_size,paddle_size):
        self.player = Player(speed=player_speed,paddle_size=paddle_size)
        self.opponent = Opponent(speed=opponent_speed,paddle_size=paddle_size)
        self.ball = Ball(speed=ball_speed, size=ball_size)
        self.score_limit = score_limit

    def start_game(self):
        pass

    def update_score(self, winner):
        pass

    def check_game_over(self):
        # determine if the game has ended and display the winner
        pass