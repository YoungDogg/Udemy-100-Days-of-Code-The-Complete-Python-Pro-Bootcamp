from turtle import Turtle
from screen import GameScreen
from gameCenter import GameCenter

from day_20.gameCenter import GameCenter


def main():
    width: int = 600
    height: int = 500

    game_center = GameCenter(width=width, height=height)
    game_center.start_game()
    game_center.screen.mainloop()



if __name__ == '__main__':
    main()
