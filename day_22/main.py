# from gameflow import GameFlow
#
#
# def main():
#     game = GameFlow(
#         score_limit=10,
#         player_speed=10, opponent_speed=10, ball_speed=3,
#         paddle_size=5, ball_size=.5,
#         width=700, height=400,
#         paddles_margin=.1
#     )
#     game.start_game()
#     game.screen.screen.mainloop()
#
#
# if __name__ == '__main__':
#     main()
from profile_util import profile_game


def main():
    profile_game()


if __name__ == '__main__':
    main()
