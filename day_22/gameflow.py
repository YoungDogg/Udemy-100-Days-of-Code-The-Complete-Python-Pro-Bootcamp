from player import Player
from opponent import Opponent
from ball import Ball
from gamescreen import GameScreen
from collision import Collision
from tools.logger import Logger
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
        self.collision = Collision()
        self.score_limit = score_limit

        # Initialize the logger
        self.logger = Logger.setup_logger('gameflow_logger', 'debug.log')
        self.logger.info("GameFlow initialized")
        self._previous_ball_pos = self.ball.ball.pos()
        self._previous_player_pos = self.player.paddle.pos()
        self._previous_opponent_pos = self.opponent.paddle.pos()

        # Desired frame rate
        self.frame_rate = 60  # Frames per second
        self.frame_duration = 1 / self.frame_rate

        # FPS logging
        self.frame_counter = 0
        self.start_time = time.time()

        # Game over flag
        self.is_over = False

    def start_game(self):
        self.player.key_bound(self)
        while not self.is_over:
            loop_start_time = time.time()  # Record start time of the loop
            self.update_game_state()
            self.debugging_log()
            elapsed_time = time.time() - loop_start_time  # Calculate elapsed time
            sleep_time = (
                max(0.001, self.frame_duration - elapsed_time))  # Calculate sleep time to maintain consistent frame rate
            time.sleep(sleep_time)  # Sleep for the calculated duration

            self.log_fps()

    def update_game_state(self):
        self.ball.move()
        self.collision.check_collision(ball=self.ball, screen=self.screen,
                                       player=self.player, opponent=self.opponent)
        self.screen.screen.update()

    def debugging_log(self):
        # Log only when any objects move
        current_ball_pos = self.ball.ball.pos()
        current_player_pos = self.player.paddle.pos()
        current_opponent_pos = self.opponent.paddle.pos()

        if (current_ball_pos != self._previous_ball_pos or
                current_player_pos != self._previous_player_pos or
                current_opponent_pos != self._previous_opponent_pos):
            self.logger.info(f"Ball position: {current_ball_pos}, "
                             f"Player position: {current_player_pos}, "
                             f"Opponent position: {current_opponent_pos}")

            self._previous_ball_pos = current_ball_pos
            self._previous_player_pos = current_player_pos
            self._previous_opponent_pos = current_opponent_pos

    def log_fps(self):
        self.frame_counter += 1
        current_time = time.time()
        elapsed_time = current_time - self.start_time
        if elapsed_time > 1.0:  # Log FPS every second
            fps = self.frame_counter / elapsed_time
            self.logger.info(f"FPS: {fps:.2f}")
            self.frame_counter = 0
            self.start_time = current_time

    def update_score(self, winner):
        pass

    def check_game_over(self):
        pass
