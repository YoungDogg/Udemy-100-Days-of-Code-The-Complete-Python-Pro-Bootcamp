import cProfile
import pstats
from ..gameflow import GameFlow
import asyncio


def profile_game():
    profiler = cProfile.Profile()
    profiler.enable()

    # Initialize and start the game
    game = GameFlow(
        score_limit=10,
        player_speed=10, opponent_speed=10, ball_speed=3,
        paddle_size=5, ball_size=.5,
        width=700, height=400,
        paddles_margin=.1
    )
    asyncio.run(game.start_game())
    game.screen.screen.mainloop()

    profiler.disable()
    profiler.dump_stats('game_profile.prof')
