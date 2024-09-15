import asyncio

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
        self.logger = Logger.setup_logger('gameflow_logger', 'debugging/debug.log')
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

    async def start_game(self):
        self.player.key_bound(self)
        while not self.is_over:
            loop_start_time = time.time()  # Record start time of the loop
            await self.update_game_state()
            # await asyncio.gather(
            #                      self.debugging_log(),
            #                      self.log_fps())
            await self.log_fps()

            elapsed_time = time.time() - loop_start_time  # Calculate elapsed time
            # question
            '''
            [ ] question: why it should be this: self.frame_duration - elapsed_time
            other than elapsed_time - self.frame_duration, or just self.frame_duration, elapsed_time?
            Or why does it just wait self.frame_duration ignoring the elapsed time?
            '''
            sleep_time = (
                max(0.001, self.frame_duration - elapsed_time))
            # time.sleep(sleep_time)  # Sleep for the calculated duration
            '''
            [ ] question: if it's non blocking, then can it manage fps?
            answer: 
            '''
            await asyncio.sleep(sleep_time)

    async def update_game_state(self):
        await asyncio.gather(
            self.ball.move(),
            self.collision.check_collision(ball=self.ball, screen=self.screen,
                                           player=self.player, opponent=self.opponent)
        )

        self.screen.screen.update()

    async def debugging_log(self):
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

    async def log_fps(self):
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
