import asyncio

COL_MARGIN = 20
PADDLE_MARGIN = 40


class Collision:

    @staticmethod
    async def handle_ball_screen_collision(ball, screen):
        # Calculate new ball direction when it hits the screens edges
        # split screen y-coordinate into upper and down screen
        screen_y = screen.get_screen_size[1] / 2
        # by absolute value
        ball_y = abs(ball.ball.pos()[1])
        if screen_y - ball_y < 10:
            ball.bounce_2_wall()

    @staticmethod
    async def handle_ball_paddle_collision(ball, player, opponent):
        # the ball with the player side
        if ball.ball.pos()[0] > 0:
            if ball.ball_distance(player.paddle) < COL_MARGIN:
                ball.bounce_2_paddle(player.paddle)
        # the ball with the opponent side
        elif ball.ball.pos()[0] < 0:
            if ball.ball_distance(opponent.paddle) < COL_MARGIN:
                ball.bounce_2_paddle(opponent.paddle)
            await opponent.chase_ball(ball)

    @staticmethod
    async def handle_paddle_screen_collision(player, opponent, screen):
        screen_x, screen_y = screen.get_screen_size
        screen_y = screen_y / 2
        # do not make paddle cross screen
        # consider two paddles, up & down screen
        if screen_y - abs(player.pos[1]) < PADDLE_MARGIN:
            player.speed(0)
        if screen_y - abs(opponent.pos[1]) < PADDLE_MARGIN:
            opponent.speed(0)

    async def check_collision(self, ball, screen, player, opponent):
        await asyncio.gather(self.handle_ball_screen_collision(ball, screen),
                             self.handle_ball_paddle_collision(ball, player, opponent),
                             self.handle_paddle_screen_collision(player, opponent, screen))
