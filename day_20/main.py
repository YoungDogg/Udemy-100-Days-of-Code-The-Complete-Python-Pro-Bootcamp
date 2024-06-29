from turtle import Turtle
from Screen import GameScreen
from GameCenter import GameCenter


from day_20.GameCenter import GameCenter


def main():
    width: int = 600
    height: int = 400

    gameCenter: GameCenter = GameCenter(width=width, height=height)
    screen = gameCenter.screen

    screen.mainloop()


if __name__ == '__main__':
    main()