from gameflow import GameFlow


def main():
    game = GameFlow(
        score_limit=10,
        player_speed=10, opponent_speed=10, ball_speed=10,
        paddle_size=5, ball_size=10,
        width=700, height=400,
        paddles_margin=.1
    )
    game.start_game()
    game.screen.screen.mainloop()
    pass


if __name__ == '__main__':
    main()
