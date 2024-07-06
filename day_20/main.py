from turtle import Turtle
from Screen import GameScreen
from GameCenter import GameCenter

from day_20.GameCenter import GameCenter


def main():
    width: int = 300
    height: int = 300

    game_center: GameCenter = GameCenter(width=width, height=height)
    screen = game_center.screen
    game_center.start_game()

    screen.mainloop()


if __name__ == '__main__':
    main()
