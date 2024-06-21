from turtle import Screen
from day_19.turtle_race.day_19_game import TurtleGame


def run_turtle_game():
    game = TurtleGame()
    game.start_game()
    game.run_turtle()
    game.end_game()
    game.screen.mainloop()


if __name__ == '__main__':
    run_turtle_game()
