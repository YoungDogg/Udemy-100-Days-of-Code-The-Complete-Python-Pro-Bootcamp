COL_MARGIN = 12
PADDLE_MARGIN = 40

import asyncio

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
        # Calculate new ball direction and speed based on the collision
        # calculate x-coordinates of both ball and paddle.
        # make both absolute value
        # should check if the ball hits the either paddles
        # measuring distance any object touches. Decide the object by ball's x-coordinate
        if ball.ball.pos()[0] > 0:
            if ball.ball_distance(player.paddle) < COL_MARGIN:
                ball.bounce_2_paddle(player.paddle)
        elif ball.ball.pos()[0] < 0:
            opponent.chase_ball(ball)
            if ball.ball_distance(opponent.paddle) < COL_MARGIN:
                ball.bounce_2_paddle(opponent.paddle)

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
        await self.handle_ball_screen_collision(ball, screen)
        await self.handle_ball_paddle_collision(ball, player, opponent)
        await self.handle_paddle_screen_collision(player, opponent, screen)
