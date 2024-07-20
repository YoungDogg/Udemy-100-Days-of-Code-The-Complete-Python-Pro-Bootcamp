from gameflow import GameFlow

def main():
    game = GameFlow(score_limit=10, player_speed=10, opponent_speed=10, ball_speed=10, ball_size=10, paddle_size=10, width=400, height=600)
    game.start_game()
    pass

if __name__ == '__main__':
    main()