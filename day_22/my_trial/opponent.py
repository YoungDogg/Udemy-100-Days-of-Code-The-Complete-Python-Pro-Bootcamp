import asyncio

from paddle import Paddle


class Opponent(Paddle):
    def __init__(self, speed, paddle_size, screen, margin):
        super().__init__(speed, paddle_size)
        _margin = margin
        _screen_width, _ = screen.get_screen_size
        _screen_x = -_screen_width / 2 * (1 - _margin)
        _screen_y = 0
        self.pos = (_screen_x, _screen_y)  # set pos, requiring screen info

    async def chase_ball(self, ball):
        # problem: it exceeds the screen
        # When ball is in opponent side,
        _, ball_y = ball.ball.pos()
        # paddle position to follow the ball
        paddle_x, paddle_y = self.paddle.pos()
        # make paddle's y-coordinate follows ball's y-coordinate
        self.paddle.speed(self.speed / 10)
        self.paddle.goto(paddle_x, ball_y)
        await asyncio.sleep(0)
