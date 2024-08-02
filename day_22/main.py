import asyncio

from gameflow import GameFlow


def main():
    game = GameFlow(
        score_limit=10,
        player_speed=10, opponent_speed=10, ball_speed=3,
        paddle_size=5, ball_size=.5,
        width=700, height=400,
        paddles_margin=.1
    )

    '''
    [ ] question: what is the diff' 
              loop.run_until_complete(game.start_game()) vs asyncio.run(game.start_game())?
    answer: 
      
    '''
    # loop = asyncio.get_event_loop()
    #
    # try:
    #     loop.run_until_complete(game.start_game())
    # except Exception as e:
    #     print(f"Exception occurred: {e}")
    # finally:
    #     loop.close()

    asyncio.run(game.start_game())

    game.screen.screen.mainloop()


if __name__ == '__main__':
    main()
